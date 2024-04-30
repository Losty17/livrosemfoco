from typing import Any, Tuple
from core.services.service_base import ServiceBase
from reviews.models.rating import Rating
from reviews.serializers.review_serializer import review_serializer


class ListReviewsService(ServiceBase):
    def __init__(self) -> None:
        super().__init__()

    def _perform(self) -> Tuple[bool, str, Any]:
        reviews = Rating.objects.all()

        reviews_json = [review_serializer(review) for review in reviews]

        return True, "Success", reviews_json
