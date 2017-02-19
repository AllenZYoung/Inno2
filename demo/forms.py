from django import forms


class MovieSearchForm(forms.Form):
    moviename = forms.CharField(label='电影名', widget=forms.TextInput(
        attrs={'class': 'form-control input', 'placeholder': '电影名'}))
