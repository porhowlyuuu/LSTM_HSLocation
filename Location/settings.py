"""
Django settings for Location project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!gw3&@ccy8-cy-2vkf&tiusu#$4gwmz=o4^vxzy-p_qwve&mz9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'HarmonicSourceLocation'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'Location.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'Location.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'PQESM',
        'HOST': '127.0.0.1',
        'PORT': '1433',
        'USER': 'sa',
        'PASSWORD': '123456',
        'OPTIONS': {
            'driver': 'SQL Server Native Client 10.0',
            'MARS_Connection': True,
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = "/static/"
TEMPLATES_URL=os.path.join(BASE_DIR,'templates')
STATICFILES_DIRS=[
   os.path.join(BASE_DIR,'static')
]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

#配置页面参数部分***********
INDEX={"name":"主页","url":"/index"};
TOPO2MATRIX={"name":"拓扑图转为矩阵","url":"/topo2Matrix"};
HarSouLocation={"name":"基于正交匹配的谐波源定位","url":"/HarSouLocation"};
MultiHarSouLocation={"name":"基于JADE算法多谐波源定位","url":"/MultiHarSouLocation"};
MyDATABASES="PQES"
PHAR="基于正交匹配的谐波源定位";
PHMULTIHAR="基于JADE算法多谐波源定位"
INFO_CONF=[
    {'name':INDEX["name"],'url':INDEX["url"]},
    # {'name':TOPO2MATRIX["name"],'url':TOPO2MATRIX["url"]},
    # {'name':HarSouLocation["name"],'url':HarSouLocation["url"]},
    # {'name':MultiHarSouLocation["name"],"url":MultiHarSouLocation["url"]}
];
Index={'name':INDEX["name"],'url':INDEX["url"]}
SourceL=[
    {'name':HarSouLocation["name"],'url':HarSouLocation["url"]},
    {'name':TOPO2MATRIX["name"],'url':TOPO2MATRIX["url"]}
]
MultiSourL=[
    {'name':MultiHarSouLocation["name"],"url":MultiHarSouLocation["url"]}
]

INFO={'SourceL':SourceL,'MultiSourL':MultiSourL,"Index":Index,'theme':'谐波源定位与责任划分',
      "PHAR":PHAR,'PHMULTIHAR':PHMULTIHAR,
             'top':'功能栏',"dataBase":MyDATABASES,
             "topo2Matrix_url":TOPO2MATRIX,"multiHarSouLocation_url":MultiHarSouLocation["url"]
             }

#操纵数据库
CONNECTION=None
# 实验室SQLServer
# DATA_INFO={"HOST":"121.195.170.238",
#            "USER":'sa',
#            "PASSWORD":'ovo1226+2',
#            "DATABASE":'test',
#            "TABLE":"DayLoadRate"
# }


# 章涛的sqlServer
DATA_INFO={"HOST":"127.0.0.1",
           "USER":'sa',
           "PASSWORD":'123456',
           "DATABASE":'PQES',
           "Site_Table":"Site",
           "Base_Data_Table":"Base_Data"
}



# 冯函宇的sqlServer
# DATA_INFO={"HOST":"121.195.170.124",
#            "USER":'sa',
#            "PASSWORD":'fenghanyu',
#            "DATABASE":'PQES',
#            "Site_Table":"Site",
#            "Base_Data_Table":"Base_Data"
# }
#数据库返回的总数据
DATA_BASE=None
HIGH_DATA_BASE=None
LOW_DATA_BASE=None
SAFE_DATA_BASE=None




# IPCC:numpy 列表的格式
IPCC=None;
UPCC=None;
#当前数据是否为复数
IS_COMPLEX=False
#默认的窗口大小 、后移步长、筛选参数、聚类算法的参数
WINDOW=100
STEP=1
PARAMS=0.85
E=0.02