import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME')]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ.get('RENDER_EXTERNAL_HOSTNAME')]

DEBUG =False

SECRET_KEY = os.environ.get('SECRET_KEY')

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS middleware to allow cross-origin requests
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]   

CORS_ALLOWED_ORIGINS = [
    # "http://localhost:8080",  
    # "http://127.0.0.1:8080",  
    "https://karreo-sy-ss.onrender.com"
    
]
CSRF_TRUSTED_ORIGINS = [
    # "http://localhost:8080",  
    # "http://127.0.0.1:8080", 
    "https://karreo-sy-ss.onrender.com"
]

STORAGES={
    "default":{
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

DATABASES ={
    'default' : dj_database_url.config(
        default= os.environ['BATABASE_URL'],
        conn_max_age=600
    )
}