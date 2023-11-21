from collections import defaultdict
from django.core.management.base import BaseCommand
from django.conf import settings
from django.apps import apps
from django.db import models
from pathlib import Path
from typing import Union
import subprocess
import os


class Command(BaseCommand):
    FIXTURES_DIR = settings.BASE_DIR / 'fixtures'
    exclude_apps = [
        "corsheaders", "django.contrib.admin", "django.contrib.auth",
        "django.contrib.contenttypes", "django.contrib.sessions",
        "django.contrib.messages", "django.contrib.staticfiles",
        "utils", "rest_framework"
    ]

    used_fixtures = defaultdict(list)
    model_tree = dict()

    _app: str = None
    _model: str = None
    _action: str = "dump"
    _exclude_apps = []
    _exclude_models = []
    _no_deps = False
    _stand = '.'
    def __check_dir(self, path: Union[Path, str]):
        return os.path.isdir(path)

    def __create_dir(self, path: Union[Path, str]):
        if not self.__check_dir(path):
            os.makedirs(path)

    def add_arguments(self, parser):
        parser.add_argument(
            'action',
            choices=["load", "dump"],
            help="Chose action"
        )

        parser.add_argument(
            '-a',
            '--app',
            dest="app",
            help="Choose an application for dump"
        )

        parser.add_argument(
            '-m',
            '--model',
            dest="model",
            help="Choose a model for dump"
        )

        parser.add_argument(
            "--exclude-apps",
            dest="exclude_apps",
            nargs="*",
            default=[],
            help="Chose apps to exclude"
        )

        parser.add_argument(
            "--exclude-models",
            dest="exclude_models",
            nargs="*",
            default=[],
            help="Choose models to exclude"
        )

        parser.add_argument(
            '-s',
            '--stand',
            dest="stand",
            nargs="?",
            default=".",
            help="Stand"
        )

        parser.add_argument(
            '--no-deps',
            dest="no_deps",
            default=False,
            action="store_true",
            help="Do not load dependencies"
        )

    def __create_model_tree(self):
        for app in apps.get_app_configs():
            if app.name in self.exclude_apps:
                continue
            self.model_tree[app.name] = {}
            for model in app.get_models():
                model_dict = {model.__name__: []}

                for field in model._meta.local_many_to_many:
                    model_dict[model.__name__].append(
                        (field.related_model._meta.app_label, field.related_model.__name__)
                    )

                for field in model._meta.local_fields:
                    if isinstance(field, models.ForeignKey):
                        model_dict[model.__name__].append(
                            (field.related_model._meta.app_label, field.related_model.__name__)
                        )

                if model_dict[model.__name__]:
                    self.model_tree[app.name].update(model_dict)
                else:
                    self.model_tree[app.name][model.__name__] = None

    def __list_models(self):
        for app in apps.get_app_configs():
            if app.name in self.exclude_apps:
                continue
            self.model_tree[app.name] = {}
            for model in app.get_models():
                self.model_tree[app.name][model.__name__] = None

    def __recursive_action(self, app: str, model: str, relations: list):
        for rel in relations:
            _app, _model = rel
            if _model in self.used_fixtures[app]:
                continue
            if _app == app and _model == model:
                continue
            if self.model_tree[_app][_model]:
                self.__recursive_action(_app, _model, self.model_tree[_app][_model])
            self.__execute_command(_app, _model)
            self.used_fixtures[_app].append(_model)

    def __execute_command(self, app: str, model: str):
        if self._action == "dump":
            self.__dump_command(app, model)
        if self._action == "load":
            self.__load_command(app, model)

    def __dump_command(self, app: str, model: str):
        app_dir = self.FIXTURES_DIR / self._stand / app
        self.__create_dir(app_dir)
        out_file = app_dir / f"{model}.json"
        p = subprocess.run([
            "python",
            "manage.py",
            "dumpdata",
            f"{app}.{model}",
            "--format=json",
            "--indent=2",
            f"-o={out_file}"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if p.stderr:
            raise Exception(p.stderr.decode('utf-8'))
        print(f"Dumped: {app=} {model=}")

    def __load_command(self, app: str, model: str):
        app_dir = self.FIXTURES_DIR / self._stand / app
        if not self.__check_dir(app_dir):
            print(f"{app_dir=} Not Found")
            return
        p = subprocess.run(
            ["python", "manage.py", "loaddata", str(app_dir / f"{model}.json")],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if p.stderr:
            raise Exception(p.stderr.decode('utf-8'))
        print(f"Loaded: {app=} {model=}")


    def __exec_fixture_action(self):
        for app in self.model_tree:
            if self._app and self._app != app:
                continue
            if self._exclude_apps and app in self._exclude_apps:
                continue
            for model in self.model_tree[app]:
                if self._model and self._model != model:
                    continue
                if self._exclude_models and model in self._exclude_models:
                    continue
                if self.model_tree[app][model]:
                    self.__recursive_action(app, model, self.model_tree[app][model])
                self.__execute_command(app, model)
                self.used_fixtures[app].append(model)

    def handle(self, *args, **options):
        self._app = options.get("app")
        self._model = options.get("model")
        self._action = options.get("action")
        self._exclude_apps = options.get("exclude_apps", [])
        self._exclude_models = options.get("exclude_models", [])
        self._no_deps = options.get("no_deps", False)
        self._stand = options.get("stand", ".")
        self.__create_dir(self.FIXTURES_DIR)
        if self._no_deps:
            self.__list_models()
        else:
            self.__create_model_tree()
        self.__exec_fixture_action()
