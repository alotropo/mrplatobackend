

from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from djoser.views import UserViewSet


class UserViewSetCustom(UserViewSet):
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]




    
















"""second type authentication"""



# import email
# from django.shortcuts import render

# from djoser.views import UserViewSet
# from rest_framework.decorators import action
# from djoser import signals
# from djoser.conf import settings
# from djoser.compat import get_user_email

# from users.models import UserAccount
# # Create your views here.
# class UserViewSetCustom(UserViewSet):
#     def perform_create(self, serializer):
#         user = UserAccount.objects.using("mrplatoflexible").create(email="jonatas.tomazini@gmail.com",username="asdsda",password=123)
        
#         signals.user_registered.send(
#             sender=self.__class__, user=user, request=self.request
#         )
#         context = {"user": user}
#         to = [get_user_email(user)]
#         if settings.SEND_ACTIVATION_EMAIL:
#             settings.EMAIL.activation(self.request, context).send(to)
#         elif settings.SEND_CONFIRMATION_EMAIL:
#             settings.EMAIL.confirmation(self.request, context).send(to)