from django.contrib import admin
from .models import Request, CustomUser

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Request)