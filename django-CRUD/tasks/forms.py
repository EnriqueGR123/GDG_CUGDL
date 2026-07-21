from django.forms import ModelForm
from .models import task

class CreateTask(ModelForm):
    class Meta:
        model = task
        fields = ['title','description','isimportant']