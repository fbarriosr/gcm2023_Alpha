"""
Django settings for djangoCgm project.
"""

import environ
import os
from pathlib import Path

# Inicializa las variables de entorno
env = environ.Env(
    DEBUG=(bool, False)  # Define DEBUG como booleano, por defecto False
)
environ.Env.read_env()  # Lee las variables del archivo .env

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad

SECRET_KEY = env("SECRET_KEY")  # Lee SECRET_KEY del .env
DEBUG = env("DEBUG")  # Activa DEBUG según el .env
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# Seguridad adicional para producción
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'search_admin_autocomplete',
    'import_export',
    'web',
    'usuarios',
    'socios',
    'capitan',
    'secretario',
    'django_recaptcha',
    'django_cleanup.apps.CleanupConfig',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Rutas
ROOT_URLCONF = 'djangoCgm.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['usuarios/templates', 'web/templates', 'socios/templates', 'tesorero/templates'],
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

# WSGI
WSGI_APPLICATION = 'djangoCgm.wsgi.application'

# Base de Datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Alternativa para PostgreSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('POSTGRES_NAME', default='postgres'),
#         'USER': env('POSTGRES_USER', default='postgres'),
#         'PASSWORD': env('POSTGRES_PASSWORD', default='postgres'),
#         'HOST': env('POSTGRES_HOST', default='localhost'),
#         'PORT': env('POSTGRES_PORT', default=5432),
#     }
# }

# Validación de Contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Modelo de Usuario
AUTH_USER_MODEL = "usuarios.Usuario"

# Internacionalización
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Archivos Estáticos y de Medios
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'web/static'),
    os.path.join(BASE_DIR, 'socios/static'),
    os.path.join(BASE_DIR, 'capitan/static'),
    os.path.join(BASE_DIR, 'tesorero/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuración de Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_HOST_USER')  # Desde el .env
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')  # Desde el .env
EMAIL_USE_TLS = True

# reCAPTCHA
RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_PUBLIC_KEY', default='')
RECAPTCHA_PRIVATE_KEY = env('RECAPTCHA_PRIVATE_KEY', default='')

# Ajustes adicionales para desarrollo
if DEBUG:
    X_FRAME_OPTIONS = 'SAMEORIGIN'  # Permite iframes en desarrollo

# comercio
COMMERCE_CODE = env('COMMERCE_CODE')
API_KEY = env('API_KEY')

