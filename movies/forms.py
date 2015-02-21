from django import forms

class AddMovie(forms.Form):
    title = forms.CharField(label='Title', max_length=120)
    release_year = forms.CharField(label='Release_Year', max_length=120)
    locations = forms.CharField(label='Location', max_length=120)
    production_company = forms.CharField(label='Production_Company', max_length=120)