from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):  # noqa: D101

    phone = PhoneNumberField('Номер телефона', null=True, blank=True)

    def __str__(self):  # noqa: D105
        return self.username
