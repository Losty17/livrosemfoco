from typing import Any, Tuple
from books.models.book import Book
from core.services.service_base import ServiceBase
from reviews.models.rating import Rating
from reviews.models.review import Review
from reviews.serializers.review_serializer import review_serializer
from django.contrib.auth.models import User


class UpsertReviewService(ServiceBase):
    def __init__(
        self,
        title: str,
        content: str,
        book_id: int,
        user: User,
    ) -> None:
        super().__init__()

        self.title = title
        self.content = content
        self.book_id = book_id

    def _perform(self) -> Tuple[bool, str, Any]:
        book = Book.objects.get(id=self.book_id)

        review = Review.objects.create(
            title=self.title,
            content=self.content,
        )

        review.save()

        rating = Rating.objects.create(
            book=book,
            review=review,
            stars=5,
        )

        rating.save()

        return True, "Book created successfully", review_serializer(rating)
