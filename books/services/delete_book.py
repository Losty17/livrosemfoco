from books.models.book import Book
from core.services.service_base import ServiceBase


class DeleteBookService(ServiceBase):
    def __init__(self, id: int) -> None:
        super().__init__()

        self.id = id

    def _perform(self):
        book = self._get_book()
        book.delete()  # todo: cascade delete reviews

        return True, "Book deleted successfully", None

    def _get_book(self):
        if not self.id:
            return False, "Book id not provided", None

        book = Book.objects.filter(id=self.id).first()

        if not book:
            return False, "Book not found", None

        return book
