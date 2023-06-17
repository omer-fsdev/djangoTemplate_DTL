from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BasicForm, StudentForm

# Create your views here.
def view_simple(request):
    return HttpResponse('<h1>Hello, that is a simple view!</h1>')

def view_simple_template(request):
    # return render(request, 'html file to render', 'variables(dict format) to use in html file')
    return render(request, 'view_simple_temp.html')

def view_template(request):
    context = {
        'title': 'test successful',
        'number': '123',
        'list': ['FS', 'DS', 'AWS'],
        'tuple': ('a', 'b', 'c'),
        'dict' : {
            'key1': 'key1 description',
            'key2': 'key2 description',
            'key3': 'key3 description',
        }
    }
    return render(request, 'view_template.html', context)

def view_form_template(request):
    form = BasicForm
    context = {
        'form': form,
        'message': 'test message',
    }
    return render(request, 'view_form_temp.html', context)

def view_student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.image = form.cleaned_data['image']
            student.save()
            return redirect('view_template')  # place the appropriate URL or view name
    else:
        form = StudentForm()

    context = {
        'form': form,
        'message': '',
    }
    return render(request, 'view_student_form.html', context)