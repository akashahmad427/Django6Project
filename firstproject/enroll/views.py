from django.shortcuts import render
from .models import Student
from .forms import Studentforms
# Create your views here.
def student(request):
    if request.method == 'POST':
        fm = Studentforms(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            roll_no = fm.cleaned_data['roll_number']
            email = fm.cleaned_data['email']
            print('My name is = ',name)
            print('roll number = ',roll_no)
            print('Email = ',email)
            fm.save()
            form = Student.objects.all() 
            return render(request,'second.html',{'name':name,'forms':form})
    else:
        fm = Studentforms()
    return render(request,'first.html',{'form':fm})


