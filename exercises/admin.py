from django.contrib import admin
from .models import Question,ListExercise,ListChallenge,QuestionChallenge
# Register your models here.


admin.site.register(QuestionChallenge)
@admin.register(ListChallenge)
class SimulateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("list_name",)}


admin.site.register(Question)
@admin.register(ListExercise)
class SimulateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("list_name",)}