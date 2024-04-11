from django.urls import path

from books import views

app_name = "books"
urlpatterns = [
    path("", views.book_router, name="book_router"),
    path("<int:pk>/", views.id_book_router, name="id_book_router"),
]
