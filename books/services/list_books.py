from typing import Any, Tuple
from books.serializers.serialize_book import serialize_book
from core.services.service_base import ServiceBase
from books.models import Book


class ListBooksService(ServiceBase):
    def __init__(self):
        super().__init__()

    def _perform(self) -> Tuple[bool, str, Any]:
        book_list = Book.objects.all()

        json = [serialize_book(book) for book in book_list]

        return True, "Books listed successfully", json
