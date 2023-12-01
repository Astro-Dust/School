from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def student_page(request):
    template = loader.get_template('student-page.html')
    return HttpResponse(template.render())

def show_students(request):

    students = {
        'Ana':19,
        'Lucas':24,
        'Carlos':23
    }

    context = {
        'students': students.items() # convertendo o dicionario para uma lista de tuplas
    }

    return render(request, 'student-page.html', context)

