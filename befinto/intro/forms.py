from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=200, label='Title')
    author = forms.CharField(max_length=100, label='Author')
    publication_date = forms.DateField(label='Publication Date')
    price = forms.DecimalField(max_digits=5, decimal_places=2, label='Price')
