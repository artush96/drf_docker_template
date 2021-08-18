from django.contrib import admin
from django.contrib.auth.models import Group

from apps.roles.models import Roles


admin.site.unregister(Group)


@admin.register(Roles)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'updated', 'created']
    list_display_links = ['id', 'name']
    filter_horizontal = ('permissions',)
