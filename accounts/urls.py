from django.urls import path
from .views import register_view, logout_view, account_settings_view, login_view, my_account_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('settings/', account_settings_view, name='account_settings'),
    path('login/', login_view, name='login'),
    path('my-account/', my_account_view, name='my_account'),
]