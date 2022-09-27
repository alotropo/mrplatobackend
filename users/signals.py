from django.dispatch import receiver
from django.db.models.signals import post_save
import json


from .models import RegisterStudents,UserAccount
from django.core.mail import send_mail
from django.conf import settings

from .list_email import create_list_email

@receiver(post_save, sender=RegisterStudents)
def my_call(sender,instance,created,**kwargs):
    
    if created and create_list_email() != None:
        
        archive = instance.archive.open()
        data = json.load(archive)


        for z in data["dict"]:
            user = UserAccount.objects.create_superuser(email=z["email"],username=z["name"],password=str(z["matricula"]),matriculation=z["matricula"])
            user.is_superuser = False
            user.save()

        message = "Welcome to Mrplato Platform. The Password is your matriculation. Good studies!"
        send_mail(subject="You have been successfully registered in mrplato", message = message, from_email=settings.EMAIL_HOST_USER,recipient_list=create_list_email())


        
