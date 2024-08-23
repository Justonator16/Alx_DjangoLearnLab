from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=50)
    publication_year = forms.DateField()
