from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50)
    school_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    

    def __str__(self):
        return f"{self.name} ({self.registration_number})"


class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    answers = models.JSONField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result: {self.student.name} - {self.score}/{self.total_questions}"
