from django.urls import path

from src.apps.profiles.views import APIRegistrationView

app_name = 'profiles'

urlpatterns = [
    path('create/', APIRegistrationView.as_view(), name='profile_register')
]
