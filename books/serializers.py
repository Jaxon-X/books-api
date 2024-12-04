from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields= '__all__'


    def validate_title(self, value):
        if not value.isalpha() or not value:
            raise serializers.ValidationError("Title must be alphanumeric")
        return value

    # def validate_price(self, value):
    #     if not value.isnumeric() or value <= 0:
    #         raise serializers.ValidationError("Price must be numeric")
    #     return value



