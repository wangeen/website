import django_tables2 as tables
import itertools
from app_my_restaurant.models import my_restaurant_desk_model

TEMPLATE = '''
    <a href="{% url  %}" class="tbl_icon edit">Edit</a>
    <a href="" class="tbl_icon delete">Delete</a>
'''

class desk_table(tables.Table):
    # row number for table
    row_number = tables.Column(empty_values=())
    def render_row_number(self):
        return 'Row %d' % next(self.counter)

    user = tables.Column(visible=False) # hide foreign key
    desk_name = tables.Column(verbose_name="Name")
    desk_person_count = tables.Column(verbose_name="Person Count")
    desk_description = tables.Column(verbose_name="Description")
    editable = tables.LinkColumn('edit_form', verbose_name='edit',  attrs={

    })
    column_name = tables.TemplateColumn(TEMPLATE)

    def __init__(self,  *args,  **kwargs):
        super(desk_table,  self).__init__(*args,  **kwargs)
        self.counter = itertools.count()

    class Meta:
        model = my_restaurant_desk_model
        attrs = {
            'class':'table table-striped'
        }
        pass
    pass
