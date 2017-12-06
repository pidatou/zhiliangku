# encoding: utf8
"""
Django settings for zhiliangku project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import ConfigParser
import sys
from lib import util

reload(sys)
sys.setdefaultencoding('utf-8')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = ConfigParser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'conf/zhiliangku.conf'))

util.set_logging(config.get('log', 'logpath'), config.get('log', 'log_level'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cq1(jfme)cw5a!glod@sjpw78+82j+ygg8ut_=i!6-r^t4k_7e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django_select2',
    'colorfield',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'zhiliangku',
    'applications.interview_question',
    'applications.slideshow',
    'applications.live_streaming',
    'applications.tracks_learning',
    'applications.custom_user',
    'applications.company_jobs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zhiliangku.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'zhiliangku.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {}
if config.get('db', 'engine') == 'mysql':
    DB_HOST = config.get('db', 'host')
    DB_PORT = config.get('db', 'port')
    DB_USER = config.get('db', 'user')
    DB_PASSWORD = config.get('db', 'password')
    DB_DATABASE = config.get('db', 'database')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': DB_DATABASE,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
            'OPTIONS': {
                'charset': 'utf8',
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            }
        }
    }
elif config.get('db', 'engine') == 'sqlite':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
STATICFILES_DIRS = (
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("js", os.path.join(STATIC_ROOT, 'js')),
    ("images", os.path.join(STATIC_ROOT, 'images')),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

tinymce_js = [
    '/static/tinymce/js/jquery.min.js',  # 必须首先加载的jquery，手动添加文件
    '/static/tinymce/js/tinymce/tinymce.min.js',  # tinymce自带文件
    '/static/tinymce/js/tinymce/plugins/jquery.form.js',  # 手动添加文件
    '/static/tinymce/js/tinymce/textarea.js',  # 手动添加文件，用户初始化参数
]

DATETIME_FORMAT = 'Y-m-d H:i:s'
DATE_FORMAT = 'Y-m-d'
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': '智量酷',
    'HEADER_DATE_FORMAT': 'Y-m-d',
    'HEADER_TIME_FORMAT': 'H:i:s',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True，自动将星号符号*添加到每个必填字段标签的末尾
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True，当您尝试离开页面时，将显示警报，而不是先保存更改的表格

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        {'app': 'auth', 'icon': 'icon-lock', 'models': ('user', 'group')},

        # {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
        # {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},

        # 用户管理
        {'app': 'custom_user', 'models': ('CustomUser', 'CustomUserAuths', 'CustomUserPath')},

        # 职业路径
        {'app': 'tracks_learning', 'models': ('Path', 'PathStage', 'CourseCategory')},

        # 课程
        {'label': '课程', 'app': 'tracks_learning', 'models': ('Course', 'Section', 'CoursePath', "Technology")},

        # 直播
        {'app': 'live_streaming'},

        # 轮播图
        {'app': 'slideshow'},

        # 企业面试题
        {'app': 'interview_question'},

        # 公司招聘职位
        {'app': 'company_jobs'},
    ),

    # misc
    # 'LIST_PER_PAGE': 15
}
