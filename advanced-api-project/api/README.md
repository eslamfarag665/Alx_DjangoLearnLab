## API Views Documentation

- **GET /books/**: Retrieves a list of all books. Available to both authenticated and unauthenticated users.
- **POST /books/**: Creates a new book. Only available to authenticated users.
- **GET /books/<id>/**: Retrieves a specific book by ID.
- **PUT /books/<id>/**: Updates a specific book. Only available to authenticated users.
- **DELETE /books/<id>/**: Deletes a specific book. Only available to authenticated users.

### Permissions:
- List and detail views are open to the public.
- Creation, update, and deletion require authentication.
 
