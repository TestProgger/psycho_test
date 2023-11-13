import logging
from typing import Callable
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, serializers
import functools
from django.http.response import HttpResponse

def normalize_data_to_log(data: dict):
    normalized_data = {}
    for key, value in data.items():
        if key in ('password', 'login', 'confirmPassword', 'username', 'email', 'confirmation_password'):
            normalized_data[key] = '********************'
        else:
            normalized_data[key] = value

    return normalized_data

def log_viewset_action(logger: logging.Logger):
    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(self, *args, **kwargs):
            request: Request = args[0]
            payload = {'kwargs': kwargs, 'query_params': request.query_params, 'data': normalize_data_to_log(request.data)}
            logger.info(
                f"{request.method} | {request.subject} | {self.__class__.__name__} | {func.__name__} payload={payload}"
            )
            try:
                response: Response = func(self, *args, **kwargs)
            except serializers.ValidationError as ex:
                logger.error(
                    f"{request.method} | {request.subject} | {self.__class__.__name__} | {func.__name__} exception={str(ex)}"
                )
                return Response(
                    data={
                        'body': None,
                        'status': {
                            'message': ex.detail,
                            'code': status.HTTP_400_BAD_REQUEST
                        }
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            except Exception as ex:
                logger.error(
                    f"{request.method} | {request.subject} | {self.__class__.__name__} | {func.__name__} exception={str(ex)}"
                )
                return Response(
                    data={
                        'body': None,
                        'status': {
                            'message': str(ex),
                            'code': status.HTTP_400_BAD_REQUEST
                        }
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            logger.info(
                f"{request.method} | {request.subject} | {self.__class__.__name__} | {func.__name__} response={normalize_data_to_log(response.data)}")

            return response
        return _wrapper
    return _decorator