from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("core/", include("core.urls", namespace="core")),
    path("auth/", include("authentication.urls", namespace="auth")),
    path("books/", include("books.urls", namespace="books")),
    path("reviews/", include("reviews.urls", namespace="reviews")),
]
