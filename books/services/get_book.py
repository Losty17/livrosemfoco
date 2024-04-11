from books.models.book import Book
from books.serializers.serialize_book import serialize_book
from core.services.service_base import ServiceBase


class GetBookService(ServiceBase):
    def __init__(self, id: int) -> None:
        super().__init__()

        self.id = id

    def _perform(self):
        book = self._get_book()

        return True, "Book retrieved successfully", serialize_book(book)

    def _get_book(self):
        if not self.id:
            return False, "Book id not provided", None

        book = Book.objects.filter(id=self.id).first()

        if not book:
            return False, "Book not found", None

        return book
