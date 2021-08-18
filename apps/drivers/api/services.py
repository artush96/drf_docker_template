from apps.drivers.models import Location
from apps.users.models import User


def get_auto_assign_driver():
    return User.drivers.last()


def socket_location(self, location):
    Location.objects.update_or_create(
        driver_id=self.driver_id,
        defaults={
            'latitude': location['latitude'],
            'longitude': location['longitude']
        }
    )
