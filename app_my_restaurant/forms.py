from django import forms

class restaurant_name_form(forms.Form):
    restaurant_name = forms.CharField(max_length=100,
                                      widget=forms.TextInput(attrs={'placeholder': 'Please Input Your Restaurant Name',
                                                                    'class': 'form-control'
                                                                   }))
    restaurant_description = forms.CharField(required=False,
                                             widget=forms.Textarea(attrs={'placeholder': 'Please Input Your Restaurant Desciption',
                                                                    'class': 'form-control'
                                                                         }))
    pass

class restaurant_add_desk_form(forms.Form):
    desk_name = forms.CharField(max_length=100,
                                      widget=forms.TextInput(attrs={'placeholder': 'Desk Name',
                                                                    'class': 'form-control'
                                                                   }))
    desk_person_count = forms.IntegerField(
                                      widget=forms.TextInput(attrs={'placeholder': 'Person Count',
                                                                    'class': 'form-control'
                                                                   }))
    desk_description = forms.CharField(max_length=100,
                                      widget=forms.TextInput(attrs={'placeholder': 'Desk description',
                                                                    'class': 'form-control'
                                                                   }))


    pass

