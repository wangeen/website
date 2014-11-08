from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

#class my_manager(models.Manager):
#    def get_query_set(self):
#        default_queryset = super(my_manager, self).get_query_set()
#        return default_queryset.filter(user=)


# Create your models here.
class my_restaurant_info_model(models.Model):
    user = models.OneToOneField(User)
    restaurant_name = models.CharField(max_length=100, default="")
    restaurant_description = models.TextField(default="")
    pass

class my_restaurant_desk_model(models.Model):
    user = models.ForeignKey(User)
    # desk name should be unqiue, it's not a good idea here use name as primary
    # key, because it's hard to select item by a complex string
    desk_name = models.CharField(unique=True, max_length=100, default="")
    desk_person_count = models.PositiveIntegerField(default="2")
    desk_description = models.CharField(max_length=100, default="")

    sort_id = models.IntegerField()

    @classmethod
    def my_insert(cls):
        pass

    @classmethod
    def my_remove(cls):
        pass

    @classmethod
    def my_up(cls):
        pass

    @classmethod
    def my_down(cls):
        pass
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
