"""
WSGI config for models_simulator project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'models_simulator.settings')

# application = get_wsgi_application()


import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
tf.config.set_visible_devices([], 'GPU')


from django.core.wsgi import get_wsgi_application
from helpers.credentials import dev_prod

dev_prod()

application = get_wsgi_application()

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'srms_project.settings')

# configuration for heroku
######################
from whitenoise import WhiteNoise
# from whitenoise.django import DjangoWhiteNoise
application = WhiteNoise(application)
#######################

