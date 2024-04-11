import json

from django.http import JsonResponse
from books.services.delete_book import DeleteBookService
from books.services.get_book import GetBookService
from books.services.upsert_book import UpsertBookService


def id_book_router(request, pk):
    if request.method == "GET":
        return GetBookService(id=pk).perform()

    if request.method == "DELETE":
        return DeleteBookService(id=pk).perform()

    if request.method == "POST":
        body = json.loads(request.body)

        title = body.get("title")
        author = body.get("author")
        publication_year = body.get("publication_year")
        isbn = body.get("isbn")
        publisher = body.get("publisher")

        success, detail, book = UpsertBookService(
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
