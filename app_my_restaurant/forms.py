from django import forms

class restaurant_name_form(forms.Form):
    restaurant_name = forms.CharField(max_length=100)
    pass
