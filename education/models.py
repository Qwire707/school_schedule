from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    subject = models.ManyToManyField(Subject, related_name="teachers")
    experience = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [("first_name")], [("last_name")]

class Class(models.Model):
    name = models.CharField(max_length=50, unique=True)
    students_count = models.PositiveIntegerField()
    class_teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)
    class_number = models.ForeignKey(Class, related_name="stutents", on_delete=models.CASCADE)

    class Meta:
        unique_together = [("first_name")], [("last_name")]





