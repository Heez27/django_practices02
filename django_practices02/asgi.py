"""
ASGI config for django_practices02 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_appl
import os #추가
from django.core.asgi import get_asgi_application #추가

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_practices02.settings')

application = get_asgi_application()
