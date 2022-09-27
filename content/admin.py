from django.contrib import admin



from content.models import Content
# Register your models here.


@admin.register(Content)
class SimulateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("topic",)}