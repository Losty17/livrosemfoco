from typing import Any, Dict
from reviews.models.rating import Rating


def review_serializer(review: Rating) -> Dict[str, Any]:
    return {
        "id": review.id,
        "book_id": review.book.id,
        "book_title": review.book.title,
        "rating": review.stars,
        "author": review.user.username,
        "review": {
            "id": review.review.id,
            "title": review.review.title,
            "content": review.review.content,
        },
        "created_at": review.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": review.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
    }
