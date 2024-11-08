from django import forms
from .models import Employee_details

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee_details
        fields = ['first_name', 'last_name', 'phone_number', 'salary','experience','roles','work_type'] 