from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(f"Book created: {book}")
# Expected output: Book created: 1984
