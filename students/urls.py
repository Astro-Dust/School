from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_page, name='students'),
    path('show_students/', views.show_students, name='show_students')
]
