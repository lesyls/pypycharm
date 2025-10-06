from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students_page, name='students'),
    path('groups/', views.groups_page, name='groups'),
    path('journal/', views.journal_page, name='journal'),
    path('teachers/', views.teachers_page, name='teachers'),
    path('predmets/', views.predmets_page, name='predmets'),
]