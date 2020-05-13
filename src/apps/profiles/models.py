from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False)
    profile_image = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()
