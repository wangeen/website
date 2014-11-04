from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
class my_restaurant_info_model(models.Model):
    user = models.OneToOneField(User)
    restaurant_name = models.CharField(max_length=100, default="")
    restaurant_description = models.TextField(default="")
    pass

class my_restaurant_desk_info(models.Model):
    user = models.ForeignKey(User)
    desk_name = models.CharField(max_length=100, default="")
    desk_person_count = models.IntegerField(default="2")
    desk_description = models.CharField(max_length=100, default="")
    pass


class my_restaurant_info_form(ModelForm):
    # TODO form for restaurant info
#    restaurant_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
#        max_length=100,
#        required=True,
#        help_text='Please set your restaurant name')
    class Meta:
        model = my_restaurant_info_model
    pass

# tutorial/models.py
class Person(models.Model):
    name = models.CharField(max_length = 100,verbose_name="full name")
