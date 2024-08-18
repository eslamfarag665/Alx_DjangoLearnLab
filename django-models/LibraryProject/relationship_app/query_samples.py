from relationship_app.models import Author, Book, Library

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.book_set.all()  # Using related_name (book_set) for ManyToManyField

# List all books in a library
def get_books_in_library(library