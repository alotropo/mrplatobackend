from django.contrib import admin
from .models import Question,ListExercise
# Register your models here.
admin.site.register(Question)



@admin.register(ListExercise)
class SimulateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("list_name",)}