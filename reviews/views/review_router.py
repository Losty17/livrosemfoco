from django.http import HttpRequest
import json
from django.http import HttpRequest, HttpResponse, JsonResponse

from authentication.models.sessions import Session
from reviews.services.list_reviews import ListReviewsService
from reviews.services.upsert_review import UpsertReviewService


def review_router(request: HttpRequest):
    if request.method == "GET":
        success, detail, json_data = ListReviewsService().perform()

        if success:
            return JsonResponse({"detail": detail, "reviews": json_data})
        else:
            return JsonResponse({"detail": detail}, status=400)

    if request.method == "POST":
        body = json.loads(request.body)

        title = body.get("title")
        content = body.get("content")
        book_id = body.get("book_id")

        auth_token = request.headers.get("Authorization").split(" ")[1]
        session = Session.objects.get(session_key=auth_token)
        user = session.user

        success, detail, book = UpsertReviewService(
            title=title,
            content=content,
            book_id=book_id,
            user=user,
        ).perform()

        return JsonResponse(
            {"success": success, "detail": detail, "book": book},
            status=200 if success else 400,
        )

    return HttpResponse(status=405)
