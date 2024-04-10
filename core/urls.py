from django.urls import path

from core.views.get_user import get_user

app_name = 'core'
urlpatterns = [
    path('user/<int:id>/', get_user, name='get_user'),
]