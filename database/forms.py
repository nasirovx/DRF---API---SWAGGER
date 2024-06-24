from django.forms import ModelForm, Textarea, CheckboxInput,TextInput, Select
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['title', 'content', 'is_published', 'cat']
        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название"
            }),
            'content': Textarea(attrs={
                'class': "form-control",
                'placeholder': "Текст"
            }),
            'is_published': CheckboxInput(),
            'cat': Select(attrs={
                'class': "form-control",
            }),
        }
        