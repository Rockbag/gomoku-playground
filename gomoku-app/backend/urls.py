from django.contrib import admin
from django.urls import path

from api.user import views as user_views
from api.game import views as game_views
import views as generic_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register/', user_views.create_user),
    path('game/', game_views.create_game),
    path('csrf/', generic_views.csrf_token)
]
