"""
Django settings for myexercisesite project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '90*+%(h5y&vxr3zfr1mdg64a!*dwfj6ny_e)7q&@bmln^yg3hr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

APPEND_SLASH = False

ACCOUNT_EMAIL_VERIFICATION = 'none'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ASGI_APPLICATION = 'myexercisesite.asgi.application'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

#ACCOUNT_ADAPTER = 'project.users.adapter.MyAccountAdapter'

ALLOWED_HOSTS = ['.myexercisesite.herokuapp.com']
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

#CHATTER_BASE_TEMPLATE="account/base.html"
# Application definition

CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_SECURE = True

INSTALLED_APPS = [
    'project.apps.ProjectConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'django.contrib.postgres'
]

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myexercisesite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'project', 'templates', 'allauth')],
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

WSGI_APPLICATION = 'myexercisesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    # 'default': {
    # 'ENGINE': 'django.db.backends.postgresql',
    # 'NAME': 'dbproject',
    # 'USER': 'groupname',
    # 'PASSWORD': 'dj@ng0p@ss',
    # }
    # 'default': {
    # 'ENGINE': 'django.db.backends.postgresql',
    # 'NAME': 'dbproject',
    # 'USER': 'groupname',
    # 'PASSWORD': 'dj@ng0p@ss',
    # }

    'default': {
    'HOST': 'ec2-100-24-139-146.compute-1.amazonaws.com',
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'degt581teja1h7',
    'USER': 'gysfjpxtctjfvz',
    'PASSWORD': 'c771aa724eed3c74bc2b2d747e99f229e0edcc340cc7e2499ee0bf0046085d9c',
    'PORT': '5432'
    }
    # 'default': {
    # 'HOST': 'ec2-54-225-190-241.compute-1.amazonaws.com',
    # 'ENGINE': 'django.db.backends.postgresql',
    # 'NAME': 'dfg5rivjq5hgi1',
    # 'USER': 'lmojgtvldrhgxy',
    # 'PASSWORD': 'bbdc923017a5007a0db776c71cc41eeb362cd2eba0fb2bc0f73db524d04be8a2',
    # 'PORT': '5432'
    # }
}

# import sys
# if 'test' in sys.argv:
#     DATABASES['default'] = {
        
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'dbproject',
#     'USER': 'groupname',
#     'PASSWORD': 'dj@ng0p@ss',
        
#     }
CHANNEL_LAYERS = {
  'default': {
      'BACKEND': 'channels_redis.core.RedisChannelLayer',
      'CONFIG': {
        'hosts': [('127.0.0.1', 6379)],
      },
  },
}
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '764512694538-8htpm7tgpbc477vq2e0nkdpsrleq346k.apps.googleusercontent.com',
            'secret': 'aVKSWeTqCOxctCi-ae_ZHzew',
            'key': ''
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

#SECURE_SSL_REDIRECT = False

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True

# os.path.join(BASE_DIR, 'static')

# Activate Django-Heroku.
try:
    # Configure Django App for Heroku.
    import django_heroku
    django_heroku.settings(locals())
except ImportError:
    found = False
