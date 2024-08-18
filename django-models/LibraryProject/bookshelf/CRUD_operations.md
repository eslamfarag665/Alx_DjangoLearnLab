#This md file contains combined CRUD operations and Documentations

#create CRUD operation in create.md file
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(f"Book created: {book}")
# Expected output: Book created: 1984

#retrieve CRUD operation in retrieve.md file
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
# Expected output: Title: 1984, Author: George Orwell, Year: 1949

#update CRUD operation in update.md file
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated book title: {book.title}")
# Expected output: Updated book title: Nineteen Eighty-Four

#delete CRUD operation in delete.md file
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted")
print("All books:", Book.objects.all())
# Expected output:
# Book deleted
# All books: <QuerySet []>