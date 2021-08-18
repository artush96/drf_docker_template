from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from apps.choices.enums import DeviceEnum
from apps.roles.models import Group
from apps.users.enums import GenderEnums
from apps.users.managers import UserManager, DriverManager, DispatcherManager
from snippets.models.abstracts import LastModMixin
from snippets.utils.passwords import generate_alt_id

IMAGE_HELP_TEXT = _('File size no more than 1Mb, image format - JPEG, PNG, GIF.')
DEFAULT_AVATAR = 'img/avatar.png'


class User(AbstractUser):
    """User model"""

    REQUIRED_FIELDS = ['email']

    image = models.ImageField(
        _('Image'), max_length=255, null=True, upload_to='user/avatar/%Y/%m/%d',
        default='img/avatar.png', help_text=IMAGE_HELP_TEXT
    )
    email = models.EmailField(_('email address'), blank=True)
    phone = models.CharField(
        _('Phone'), max_length=11, null=True, help_text=_('Input format: 79601234567')
    )
    city = models.CharField(_('City'), max_length=100, blank=True, null=True)
    gender = models.CharField(
        _('Gender'), max_length=30, null=True,
        default=GenderEnums.NOT_AVAILABLE, choices=GenderEnums.choices
    )
    address = models.TextField(_('Address'), blank=True)
    birth_date = models.DateField(_('Birth date'), blank=True, null=True)

    is_online = models.BooleanField(_('Online'), default=True, null=True)

    is_driver = models.BooleanField(_('Driver'), default=False)
    is_dispatcher = models.BooleanField(_('Dispatcher'), default=False)

    note = models.CharField(max_length=300, verbose_name=_('Note'))
    device_platform = models.CharField(
        max_length=7, choices=DeviceEnum.choices,
        blank=True, verbose_name=_('Device platform')
    )
    verified = models.BooleanField(default=False, null=True, verbose_name=_('Verified'))
    device_api_key = models.CharField(max_length=150, null=True, verbose_name=_('Api key'))
    initial_password = models.CharField(_('Initial password'), null=True, max_length=128)

    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, null=True, related_name='employers')

    objects = UserManager()
    drivers = DriverManager()
    dispatchers = DispatcherManager()

    history = HistoricalRecords()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        unique_together = ('email', 'company')

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email.split('@')[0] + '_' + generate_alt_id(length=4)
        super(User, self).save(*args, **kwargs)

    @property
    def full_name(self):
        parts = filter(None, (self.last_name, self.first_name))
        return ' '.join(parts) or self.username


class AttachedFiles(LastModMixin):
    """User attached files Model"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='User', related_name='files')
    file = models.FileField('File', upload_to='agent/files/%Y/%m/%d')

    class Meta:
        verbose_name = _('Attached File')
        verbose_name_plural = _('Attached Files')

    def __str__(self):
        return '%s - %s' % (self.user if self.user else _('Not User'), self.file)


class UserLoginIp(LastModMixin):
    """User login ip address Model"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=_('User'), related_name='ips')
    ip = models.GenericIPAddressField(_('IP-address'), blank=True, null=True)

    class Meta:
        verbose_name = _('User Login Ip')
        verbose_name_plural = _('User Login Ips')

    def __str__(self):
        return '%s - %s' % (self.user if self.user else _('Not User'), self.ip)

