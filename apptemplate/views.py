from django.shortcuts import render

# Create your views here.

def view_temp1(request):
    context = {
        'title': 'Django Template!',
        'number': 1234,
        'dict' : {'a': '1', 'b': '2'},
        'is_exist': True,
        'list' : ['a', 'b', 'c', 'd']
    }
    return render(request, 'temp1.html', context)

def view_temp2(request):
    return render(request, 'temp2.html')