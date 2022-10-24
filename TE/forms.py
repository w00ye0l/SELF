from django import forms

LANG_CHOICES = (
    ("eng", "English"),
    ("kor", "Korean"),
    ("tel", "Telugu"),
    ("hin", "Hindi"),
)


class reqData(forms.Form):
    image = forms.ImageField()
    lang = forms.ChoiceField(choices=LANG_CHOICES)
