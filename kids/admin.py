#admin for the 'kids' django app

from django.contrib import admin
from .models import Kids, Events

# Register your models here.
admin.site.register(Kids)
admin.site.register(Events)