from django import forms
from .models import Student
class Studentforms(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id','name','email','roll_number']

