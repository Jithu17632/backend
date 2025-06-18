from rest_framework import serializers
from .models import Student, ExamResult

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'registration_number', 'school_name', 'email']

class ExamResultSerializer(serializers.ModelSerializer):
    student = StudentSerializer()

    class Meta:
        model = ExamResult
        fields = ['student', 'score', 'total_questions', 'answers', 'completed_at']

    def create(self, validated_data):
        student_data = validated_data.pop('student')

        # Use registration_number as the unique identifier
        student, created = Student.objects.get_or_create(
            registration_number=student_data['registration_number'],
            defaults={
                'name': student_data['name'],
                'school_name': student_data['school_name'],
                'email': student_data['email'],
            }
        )

        # Optional: update student info if already exists (optional logic)
        if not created:
            student.name = student_data['name']
            student.school_name = student_data['school_name']
            student.email = student_data['email']
            student.save()

        return ExamResult.objects.create(student=student, **validated_data)
