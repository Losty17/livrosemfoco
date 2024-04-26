import json
from django.http import HttpRequest, HttpResponse, JsonResponse

from books.services.delete_book import DeleteBookService
from books.services.list_books import ListBooksService
from books.services.upsert_book import UpsertBookService


def book_router(request: HttpRequest):
    if request.method == "GET":
        success, detail, json_data = ListBooksService().perform()

        if success:
            return JsonResponse({'detail': detail, 'books': json_data})
        else:
            return JsonResponse({'detail': detail}, status=400)

    if request.method == "POST":
        body = json.loads(request.body)

        title = body.get("title")
        author = body.get("author")
        publication_year = body.get("publication_year")
        isbn = body.get("isbn")
        publisher = body.get("publisher")

        success, detail, book = UpsertBookService(
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

    return HttpResponse(status=405)
