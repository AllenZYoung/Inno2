from django import forms


class MovieSearchForm(forms.Form):
    moviename = forms.CharField(required=True, label='电影名', widget=forms.TextInput(
        attrs={'class': 'form-control selltwo', 'placeholder': '电影名'}))
