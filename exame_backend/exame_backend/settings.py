from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-)pwo2e2-=*1&$#k935blnk)(#+j&#2t%#9xmr5tzkw3h4fi0e6'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'exame',
    'rest_framework',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware to allow cross-origin requests
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'exame_backend.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'details',
        'USER':'root',
        'PASSWORD':'Jithin@9746',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT=BASE_DIR/'staticfiles'
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
SESSION_COOKIE_SAMESITE = 'None'  # Required for cross-origin requests in development

# CSRF settings
CSRF_COOKIE_HTTPONLY = False  # Allow the token to be accessed by JavaScript
CSRF_COOKIE_SECURE = False  # Set to True in production with HTTPS

# CORS settings
CORS_ALLOW_CREDENTIALS = True  # Allow credentials (cookies)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",  # Allow the React frontend running on port 8080
    "http://127.0.0.1:8080",  # Allow the React frontend running on port 8080
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",  # Add frontend URL here
    "http://127.0.0.1:8080",  # (optional) add both if needed
]
