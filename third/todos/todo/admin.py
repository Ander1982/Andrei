from django.contrib import admin
from .models import Todo


class TotoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Todo, TotoAdmin)
