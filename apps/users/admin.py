from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from apps.users.models import User, UserLoginIp, AttachedFiles


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name', 'last_name', 'email', 'phone', 'note', 'device_platform',
                'verified', 'device_api_key', 'initial_password', 'company', 'image'
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'is_driver',
                'is_dispatcher', 'groups', 'user_permissions',
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('id', 'get_image', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    list_display_links = ('id', 'get_image', 'username')

    def get_image(self, obj):
        if obj.image:
            image = obj.image
            return format_html('<img src="%s" alt="" style="max-width:40px;max-height:40px;">' % (
                    image.url
                ))
        else:
            return ''

    get_image.short_description = _('Image')


@admin.register(UserLoginIp)
class UserIpAdmin(admin.ModelAdmin):
    list_display = ['user', 'ip', 'updated', 'created']


@admin.register(AttachedFiles)
class AttachedFilesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'file', 'created']
