"""
WSGI config for ziahbusiness project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

# =====================
# wsgi.py file begin 

import os, sys
# add the hellodjango project path into the sys.path
sys.path.append('/home/iskandar_amir/ziah.business/ziahbusiness')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/iskandar_amir/ziah.business/ziahbusinessenv/Lib/site-packages')

# poiting to the project settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ziahbusiness.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# wsgi.py file end
# ===================