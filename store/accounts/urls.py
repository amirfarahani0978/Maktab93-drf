from django.urls import path
from .views import UserRegister
from rest_framework.authtoken import views as auth_token


"""
add auth-token for authentication and with url can get the token about the my user.
"""
app_name = 'accounts'
urlpatterns = [
    path('register/' , UserRegister.as_view()),
    path('api-token-auth/' , auth_token.obtain_auth_token)
]   