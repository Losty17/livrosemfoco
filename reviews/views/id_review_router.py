import json
from django.http import JsonResponse
from reviews.services.delete_review import DeleteReviewService
from reviews.services.get_review import GetReviewService
from reviews.services.upsert_review import UpsertReviewService


def id_review_router(request, pk: int):
    if request.method == "GET":
        return GetReviewService(id=pk).perform()

    if request.method == "DELETE":
        return DeleteReviewService(id=pk).perform()

    if request.method == "POST":
        body = json.loads(request.body)

        title = body.get("title")
        author = body.get("author")
        publication_year = body.get("publication_year")
        isbn = body.get("isbn")
        publisher = body.get("publisher")

        success, detail, book = UpsertReviewService(
            id=pk,
            title=title,
            author=author,
            publication_year=publication_year,
            isbn=isbn,
            publisher=publisher,
        ).perform()

        return JsonResponse(
            {"success": success, "detail": detail, "book": book},
            status=200 if success else 400,
        )
