from django.shortcuts import render, redirect
from .models import Student, Group

def index(request):
    return render(request, 'main/index.html')

def students_page(request):
    return render(request, 'main/students.html')

def groups_page(request):
    return render(request, 'main/groups.html')

def journal_page(request):
    return render(request, 'main/journal.html')

def teachers_page(request):
    return render(request, 'main/teachers.html')

def predmets_page(request):
    return render(request, 'main/predmets.html')

def students_edit(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'main/students_edit.html', {'student': student})

def student_update(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(id=student_id)
        student.name = request.POST['name']
        student.phone = request.POST['phone']
        student.photo = request.POST['photo']
        student.save()
    return redirect('students_edit', student_id=student_id)

def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('students')


def students_page(request):
    # Получаем всех студентов из базы
    students = Student.objects.all()
    return render(request, 'main/students.html', {'students': students})


def student_add(request):
    if request.method == 'POST':
        # Создаем нового студента
        group, created = Group.objects.get_or_create(name=request.POST['group'])

        student = Student(
            name=request.POST['name'],
            phone=request.POST['phone'],
            photo=request.POST['photo'],
            group=group
        )
        student.save()

    return redirect('students')