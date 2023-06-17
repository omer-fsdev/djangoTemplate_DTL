
from django.urls import path
from .views import view_simple, view_simple_template, view_template, view_form_template, view_student_form

urlpatterns = [
    path('viewsimple/', view_simple, name='view_simple'),
    path('viewsimpletemp/', view_simple_template, name='view_simple_template'),
    path('viewtemplate/', view_template, name='view_template'),
    path('viewformtemp/', view_form_template, name='view_form_template'),
    path('viewstudentform/', view_student_form, name='view_student_form'),
]