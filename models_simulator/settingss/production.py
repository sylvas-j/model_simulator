from .common import *
###############
## configuration for heroku
# import dj_database_url
# import django_heroku
####################

DEBUG = True

# ALLOWED_HOSTS = ['127.0.0.1','localhost','localhost:8282','devarchive.org','www.devarchive.org','devarchive.org:8181','www.devarchive.org:8181']
ALLOWED_HOSTS = ['*']


CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8181',
    'http://devarchive.org:8181',
    'http://www.devarchive.org:8181',
]

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8181',
    'http://devarchive.org:8181',
    'http://www.devarchive.org:8181',
]

# CSRF_TRUSTED_ORIGINS = [
#     'http://localhost:8181',
#     'http://devarchive.org:8181',
#     'http://localhost',
#     'http://devarchive.org',
#     'http://www.devarchive.org:8181',
#     'http://www.devarchive.org',
# ]

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost',
#     'http://localhost:8181',
#     'http://devarchive.org:8181',
#     'http://devarchive.org',
#     'http://www.devarchive.org:8181',
#     'http://www.devarchive.org',
# ]


# TEST/DEVELOPMENT REMOTE DATABASE
# DATABASES = {
#     # 'default': {},
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'admin_mod_sim',
#         'USER': 'admin_root',
#         'PASSWORD': 'admin_sylvas',
#         'HOST': '104.37.191.201',
#         # 'HOST': 'devarchive.org',
#         'PORT': '3306',
#         # 'OPTIONS': {
#         #   'init_command': "set sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'"
#         # },
#     },
# }


# DATABASES = {
#     # 'default': {},
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'admin_mod_sim2',
#         'USER': 'admin_root2',
#         'PASSWORD': 'admin_sylvas2',
#         'HOST': '104.37.191.201',
#         # 'HOST': 'devarchive.org',
#         'PORT': '3306',
#         'OPTIONS': {
#           'init_command': "set sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'"
#         },
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




# django_heroku.settings(locals())
# django_heroku.settings(config=locals(), staticfiles=False,logging=False)

# prod_db  =  dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(prod_db)


# configuration for heroku
##################
# ADMINS = (('Webmaster','sylvanusjerome@gmail.com'))
# MANAGERS = ADMINS


