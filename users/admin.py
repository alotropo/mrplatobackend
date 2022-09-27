from django.contrib import admin

# Register your models here.

from .models import UserAccount,RegisterStudents

admin.site.register(UserAccount)
admin.site.register(RegisterStudents)
