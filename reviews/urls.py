from django.urls import path

from reviews import views

app_name = "reviews"
urlpatterns = [
    path("", views.review_router, name="review_router"),
    path("<int:pk>/", views.id_review_router, name="id_review_router"),
]
