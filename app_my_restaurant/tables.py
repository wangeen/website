import django_tables2 as tables
from app_my_restaurant.models import my_restaurant_desk_model

class desk_table(tables.Table):

    class Meta:
        model = my_restaurant_desk_model
        attrs = {
            'class':'table table-striped'
        }
        pass
    pass
