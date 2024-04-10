from django.urls import path

from authentication.views.register_user import register_user
from authentication.views.token import get_token

app_name = "authentication"
urlpatterns = [
    path("token/", get_token, name="get_token"),
    path("register/", register_user, name="register_user"),
]
