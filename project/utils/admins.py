from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):

    def _get_user_defined_readonly_fields(self, request, obj=None):
        return ()

    def get_readonly_fields(self, request, obj=None):
        return (
            *('id', ),
            *self._get_user_defined_readonly_fields(request, obj),
            *('created_at', 'updated_at')
        )