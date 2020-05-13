from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from django.contrib.auth import get_user_model

from src.apps.profiles.models import Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(required=False)
    phone_number = PhoneNumberField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth']

    def save(self, **kwargs):
        phone_number = self.validated_data.pop('phone_number')
        date_of_birth = self.validated_data.pop('date_of_birth')
        user = super(UserSerializer, self).save()
        profile, _ = Profile.objects.get_or_create(user=user)
        profile.phone_number = phone_number
        profile.date_of_birth = date_of_birth
        profile.save()
        return user
