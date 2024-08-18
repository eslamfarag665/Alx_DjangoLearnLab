from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', all_books, name='books'),
    path('library', LibraryView.as_view(), name='library')
]
