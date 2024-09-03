from rest_framework import serializers
from .models import Author, Book
import datetime as  dt

# model serializers user fields from models as input to convert into a json, xml
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        current_year = dt.datetime.year()
        if data['publication_year'] > current_year:
            raise serializers.ValidationError(f"Year must be <= {current_year}")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']