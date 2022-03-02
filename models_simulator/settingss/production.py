from .common import *
###############
## configuration for heroku
import dj_database_url
import django_heroku
####################

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost','https://model-simulator.herokuapp.com/']


# TEST/DEVELOPMENT REMOTE DATABASE
# DATABASES = {
#     # 'default': {},
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': 'db4free.net',
#         'PORT': '3306',
#         'NAME': 'sn_rsu_db',
#         'USER': 'sn_test_user',
#         'PASSWORD': 'sn_test_user',
#     },
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




django_heroku.settings(locals())
django_heroku.settings(config=locals(), staticfiles=False,logging=False)

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)


# configuration for heroku
##################
ADMINS = (('Webmaster','sylvanusjerome@gmail.com'))
MANAGERS = ADMINS


