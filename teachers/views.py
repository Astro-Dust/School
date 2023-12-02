from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here

# CRIAR UMA PAGINA INICIAL APENAS PARA PROFESSORES
def teacher_page(request):
    template = loader.get_template('teacher-page.html')
    return HttpResponse(template.render())

# ESTA VAI SER UMA OUTRA PÁGINA QUE SERVE APENAS PARA LISTAR OS PROFESSORES
def show_teachers(request):
    
    # name and experience in years
    teachers = {
        'Tom':3,
        'Sibito':10,
        'Carol':5,
        'Debora':2
    }

    context = {
        'teachers': teachers.items()
    }

    return render(request, 'teacher-page.html', context)
