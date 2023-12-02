from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.teacher_page, name='teachers'),
    path('show_teachers/', views.show_teachers, name='show_teachers')
]
