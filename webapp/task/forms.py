from django import forms
from .models import Employee


#Model Form
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
