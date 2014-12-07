import django_tables2 as tables
import itertools
from app_my_restaurant.models import my_restaurant_desk_model

# td contenteditable='true'

TEMPLATE = '''
    <a href="{% url 'my_restaurant_update_desk' desk_id=record.pk %}" class="tbl_icon edit">Edit</a>
    <a href="{% url 'my_restaurant_remove_desk' desk_id=record.pk %}" class="tbl_icon delete">Delete</a>
'''

class desk_table(tables.Table):
    # row number for table
    #row_number = tables.Column(empty_values=())
    #def render_row_number(self):
    #    return 'Row %d' % next(self.counter)

    id = tables.Column(visible=False) # hide foreign key
    user = tables.Column(visible=False) # hide foreign key
    desk_name = tables.Column(verbose_name="Name")
    desk_person_count = tables.Column(verbose_name="Person Count")
    desk_description = tables.Column(verbose_name="Description")
    # edit column
    operations = tables.TemplateColumn(TEMPLATE)

    def __init__(self,  *args,  **kwargs):
        super(desk_table,  self).__init__(*args,  **kwargs)
        #self.counter = itertools.count()

    class Meta:
        model = my_restaurant_desk_model
        attrs = {
            'class':'table table-striped'
        }
        pass
    pass
