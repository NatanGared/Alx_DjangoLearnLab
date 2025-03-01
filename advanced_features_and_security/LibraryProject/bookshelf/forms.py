from django import forms
from .models import Book, Author  # Make sure to import your models

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Specify the model you want to create the form for
        fields = ['title', 'author']  # List the fields you want in the form

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can customize your form here, for example:
        self.fields['title'].widget.attrs.update({'placeholder': 'Enter book title'})
        self.fields['author'].empty_label = "Select an Author"  # Customize the label for the author field