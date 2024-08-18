from relationship_app.models import Book, Librarian, Library

author_books = Book.objects.get(author="author name")
library_books = Book.objects.get(Library="library")
library_librarian = Book.objects.get(library="lib")