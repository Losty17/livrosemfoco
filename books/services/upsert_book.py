from typing import Any, Tuple
from books.models.book import Book
from books.serializers.serialize_book import serialize_book
from core.services.service_base import ServiceBase


class UpsertBookService(ServiceBase):
    def __init__(
        self,
        id: int = None,
        title: str = None,
        author: str = None,
        publication_year: int = None,
        isbn: str = None,
        publisher: str = None,
    ) -> None:
        super().__init__()

        self.id = id
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.publisher = publisher

    def _perform(self) -> Tuple[bool, str, Any]:
        book = self._get_book()

        book.title = self.title or book.title
        book.author = self.author or book.author
        book.publication_year = self.publication_year or book.publication_year
        book.isbn = self.isbn or book.isbn
        book.publisher = self.publisher or book.publisher

        book.save()

        return (
            True,
            "Book upserted successfully",
            serialize_book(book),
        )

    def _get_book(self):
        if self.id:
            book = Book.objects.filter(id=self.id).first()

            if not book:
                return False, "Book not found", None

            return book

        return Book()
