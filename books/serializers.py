from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price',)


    # betta xammasini tekshirsa validatsiya qisa boladi
    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)


        # check title if it contains only alpabetical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Kitobni sarvlahasi harflardan tashkil topgan bolishi kerak!"
                }
            )



        # check title and author from database existence
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Title va muallifi bir xil bolgan kitobni yuklay olmaysiz!"
                }
            )
        return data


    # buyoda aloxida aloxida tekshirsa boladi, field boyicha
    def validate_price(self, price):
        if price < 0 or price > 999999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Narx notog'ri kiritilgan!"
                }
            )




