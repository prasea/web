

from django import forms
from .models import Employee
#  In a similar way that a model class’s fields map to database fields, a form class’s fields map to HTML form <input> elements.
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'