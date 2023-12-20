from django.contrib import admin
from .models import Ex


class ExAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Ex, ExAdmin)
