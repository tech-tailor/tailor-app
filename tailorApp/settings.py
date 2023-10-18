"""
dont forget to export these to each of the enviroments
export DJANGO_SETTINGS_MODULE=tailorApp.settings_prod  # For production

export DJANGO_SETTINGS_MODULE=tailorApp.settings_dev  # For development

"""





from pathlib import Path
import os
from decouple import config
import django
from django.utils.encoding import smart_str





# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')



# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

#ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
   
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'allauth.socialaccount.providers.google',
    'django.contrib.staticfiles',
    'csp',
    'django_hosts',
    'django_inlinecss',
    "phonenumber_field",
    'work',
    'store',
    'user',

]

MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
]


django.utils.encoding.smart_text = smart_str



CSP_DEFAULT_SRC = ("'self'", "cdn.jsdelivr.net", "'unsafe-inline'")
CSP_STYLE_SRC = ("'self'", "cdn.jsdelivr.net", "https://maxcdn.bootstrapcdn.com", "fonts.googleapis.com","https://cdnjs.cloudflare.com", "https://stackpath.bootstrapcdn.com", "code.jquery.com", )
CSP_SCRIPT_SRC = ("'self'", "cdn.jsdelivr.net", "https://maxcdn.bootstrapcdn.com", "fonts.googleapis.com","https://cdnjs.cloudflare.com", "https://stackpath.bootstrapcdn.com", "code.jquery.com", )
CSP_IMG_SRC = ("'self'", "data:")
CSP_FONT_SRC = ("'self'", "cdn.jsdelivr.net", "https://maxcdn.bootstrapcdn.com", "fonts.googleapis.com","https://cdnjs.cloudflare.com", "https://stackpath.bootstrapcdn.com", "code.jquery.com", "https://fonts.gstatic.com" )

#CSP_REPORT_URI = "/product/"  #handle this in a view to monitor it

ROOT_URLCONF = 'tailorApp.urls'

ROOT_HOSTCONF = 'tailorApp.hosts'
DEFAULT_HOST = 'default'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.normpath(os.path.join(BASE_DIR, 'templates')),
            ],
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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]


#django-allauth settings
LOGIN_REDIRECT_URL= '/accounts/profile/'
ACCOUNT_AUTHENTICATION_METHOD= 'username_email'
ACCOUNT_CHANGE_EMAIL=True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=1
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_LOGOUT_REDIRECT_URL='/'
ACCOUNT_USERNAME_BLACKLIST=['jesus', 'admin', 'neeyee']
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

#ACCOUNT_FORMS = {
#
# 'signup': 'user.forms.CustomSignupForm', 
#}


#twill0 account to confirm every phonenumber
TWILIO_ACCOUNT_SID = 'AC898688ec7726160651e2772aab6d718a'
TWILIO_AUTH_TOKEN = '2b8b6df46c3c70365b0387aaa9930b04'
TWILIO_PHONE_NUMBER = '+2347065727413'





SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        },
        'APP': {
            'client_id': config('YOUR_CLIENT_ID'),
            'secret': config('YOUR_CLIENT_SECRET'),
        },
        'OAUTH_PKCE_ENABLED': True,
        
    }
}

WSGI_APPLICATION = 'tailorApp.wsgi.application'


#access the user profile directly from the User model
AUTH_USER_MODEL = 'user.CustomUser'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

SECURE_HSTS_SECONDS = 2592000
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'












