from django.contrib import admin

# Register your models here.

from .models import PhotoUser, UserAccount,RegisterStudents

admin.site.register(UserAccount)
admin.site.register(RegisterStudents)
admin.site.register(PhotoUser)



from rest_framework_simplejwt import token_blacklist

class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True # or whatever logic you want

admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)


