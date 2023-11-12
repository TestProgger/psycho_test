from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at')