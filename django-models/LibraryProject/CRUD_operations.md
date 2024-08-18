<!-- create -->

Operation: create
Commands:

```python
new_book = Book(title="1984", author="George Orwell" pulication_year=1949)

new_book.save()
```

output: ""

<!-- retrieve -->

Operation: retrieve
Commands:

```python
from bookshelf.models import Book

Book.objects.all()
```

output: "<QuerySet [<Book: Book object (1)>]>"

<!-- update -->

Operation: update
Commands:

```python
book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four"

book.save()
```

output: ""

<!-- delete -->

Operation: delete
Commands:

```python
book = Book.objects.get(title="Nineteen Eighty-Four")

book.delete()
```

output: ""
