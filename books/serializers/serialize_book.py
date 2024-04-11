from books.models.book import Book


def serialize_book(book: Book):
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "publication_year": book.publication_year,
        "isbn": book.isbn,
        "publisher": book.publisher,
        "created_at": book.created_at,
        "updated_at": book.updated_at,
        "ratings": book.rating_set.count(),
    }
