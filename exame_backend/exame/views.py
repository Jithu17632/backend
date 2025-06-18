from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render
from rest_framework import generics
from .models import ExamResult
from .serializers import ExamResultSerializer
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

# Create your views here.

@csrf_exempt
@require_POST
def admin_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid username or password'})

class SubmitExameResultView(generics.CreateAPIView):
    serializer_class = ExamResultSerializer

class GetAllResultsView(generics.ListAPIView):
    queryset = ExamResult.objects.all().order_by('-completed_at')
    serializer_class = ExamResultSerializer

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        
        if User.objects.filter(username=email).exists():
            return JsonResponse({'success': False, 'message': 'Email already registered'})
        
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name,
        )
        
        return JsonResponse({'success': True, 'message': 'Signup successful'})

@csrf_exempt
@require_POST
def login_view(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        # Find user by email
        user = User.objects.filter(email=email).first()
        if user is None:
            return JsonResponse({'success': False, 'message': 'User with this email not found'}, status=400)

        # Authenticate using username
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True, 'message': 'Login successful', 'username': user.first_name, 'email': user.email})
        else:
            return JsonResponse({'success': False, 'message': 'Incorrect password'}, status=400)

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

def check_login(request):
    if request.user.is_authenticated:
        print(f"User authenticated: {request.user.username}")
        return JsonResponse({
            'isAuthenticated': True,
            'username': request.user.first_name,
            'email': request.user.email
        })
    else:
        print("User not authenticated")
        return JsonResponse({'isAuthenticated': False})
    

@csrf_exempt
@require_POST
def logout_view(request):
    logout(request)
    return JsonResponse({'success':True,'message':'Logout successfull'})