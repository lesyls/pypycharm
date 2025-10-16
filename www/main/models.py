from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    class_teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Teacher(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    photo = models.CharField(max_length=200, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grade = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.grade}"

