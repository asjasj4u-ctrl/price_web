# price_web/settings.py

from pathlib import Path
import os

# ---------------------------
# 1- مسار المشروع الأساسي
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# 2- إعدادات الأمان
# ---------------------------
SECRET_KEY = 'YOUR_SECRET_KEY_HERE'  # ضع مفتاحك الخاص هنا
DEBUG = True  # للإختبار، قم بتغييرها إلى False في الإنتاج
ALLOWED_HOSTS = []

# ---------------------------
# 3- التطبيقات المثبتة
# ---------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'prices',
]

# ---------------------------
# 4- الميدل وير
# ---------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------------
# 5- URLs
# ---------------------------
ROOT_URLCONF = 'price_web.urls'

# ---------------------------
# 6- قوالب Templates
# ---------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # مجلد القوالب العام
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

# ---------------------------
# 7- WSGI
# ---------------------------
WSGI_APPLICATION = 'price_web.wsgi.application'

# ---------------------------
# 8- قاعدة البيانات
# ---------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # للتجربة المحلية
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ---------------------------
# 9- التحقق من كلمة المرور
# ---------------------------
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

# ---------------------------
# 10- إعدادات اللغة والمنطقة الزمنية
# ---------------------------
LANGUAGE_CODE = 'ar-sa'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# ---------------------------
# 11- إعدادات الملفات الثابتة
# ---------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# ---------------------------
# 12- الإعدادات الافتراضية للمفاتيح التلقائية
# ---------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
