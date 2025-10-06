from django.shortcuts import render

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