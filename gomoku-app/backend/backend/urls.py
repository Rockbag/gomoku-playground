from django.contrib import admin
from django.urls import path

from backend.api.user import views as user_views
from backend import views as generic_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register/', user_views.create_user),
    path('csrf/', generic_views.csrf_token)
]
