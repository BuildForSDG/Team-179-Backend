from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/profiles/v1/', include('src.apps.profiles.urls'))
]
