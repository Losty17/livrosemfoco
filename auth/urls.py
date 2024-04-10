from django.urls import path

from auth.views.token import get_token

app_name = 'auth'
urlpatterns = [
    path('token/', get_token, name='get_token'),
]