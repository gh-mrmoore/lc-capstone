#admin for the 'finances' django app

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Banks)
admin.site.register(LCat)
admin.site.register(Line)