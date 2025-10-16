from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students_page, name='students'),
    path('groups/', views.groups_page, name='groups'),
    path('journal/', views.journal_page, name='journal'),
    path('teachers/', views.teachers_page, name='teachers'),
    path('predmets/', views.predmets_page, name='predmets'),
    path('student/<int:student_id>/', views.students_edit, name='students_edit'),
    path('student/<int:student_id>/update/', views.student_update, name='student_update'),
    path('student/<int:student_id>/delete/', views.student_delete, name='student_delete'),
    path('student/add/', views.student_add, name='student_add'),
]