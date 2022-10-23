from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        labels = {
            "title": "책 제목",
            "image": "책 이미지",
            "x": "x 좌표",
            "y": "y 좌표",
        }
