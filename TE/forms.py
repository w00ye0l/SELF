from django import forms
from .models import *

LANG_CHOICES = (
    ("eng", "English"),
    ("kor", "Korean"),
    ("tel", "Telugu"),
    ("hin", "Hindi"),
)


class reqData(forms.Form):
    image = forms.ImageField()
    lang = forms.ChoiceField(choices=LANG_CHOICES)



class AudioForm(forms.ModelForm):
    class Meta:
        model=Audio_store
        fields=['record']