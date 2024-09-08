# api/serializers.py

from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Serializes all fields and includes custom validation to ensure
    the publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_publication_year(self, value):
        """
        Validate that the publication_year is not in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes the name field and a nested BookSerializer to dynamically
    serialize related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

