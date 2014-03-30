# -*- encoding: utf-8 -*-
"""
Django settings for biblioteca project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Usando unipath, sube del archivo 2 niveles (carpeta del proyecto 'biblioteca')
from unipath import Path
RUTA_PROYECTO = Path(__file__).ancestor(2)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9dw&%0r%p@4s)y+jsf$et01qu5ldiv^$bn=1(=0c0@@a323y85'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    # '/home/ronny/Programas/DjangoApps/pruebas/biblioteca/templates',
    # os.path.join(BASE_DIR,'templates'),
    # Los anteriores modos tambien funcionan
    # pero esta vez usaremos los del tutorial 5 de devcode.la
    RUTA_PROYECTO.child('templates'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'autores',
    'inicio',
)

from django.core.urlresolvers import reverse_lazy
LOGIN_URL = reverse_lazy('login')
# cap9 - Cuando me loguee en esta caso no quiero que se redirija
#        a otra url sino a esta misma
LOGIN_REDIRECT_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

MEDIA_ROOT = RUTA_PROYECTO.child('media')

MEDIA_URL = 'http://127.0.0.1:8000/media/'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'biblioteca.urls'

WSGI_APPLICATION = 'biblioteca.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# cap8 - Usare esta url para llamar mis archivos
STATIC_URL = '/static/'

# cap8 - Con esto le digo a django que uso esta carpeta
# para guardar mis archivos státicos
STATICFILES_DIRS = (
    RUTA_PROYECTO.child('static'),
)
