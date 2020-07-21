from django.forms import Form
from activities.models import Activity, Option


class ActivityForm(Form):
    class Meta:
        model = Activity
        fields = '__all__'
        # fields = ('title', 'end_datetime', )


class Option(Form):
    class Meta:
        modal = Option
        fields = ('content', 'image')
