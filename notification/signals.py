from django.dispatch import receiver
from django.db.models.signals import post_save

from notification.models import Notification
from django.core.mail import send_mail
from django.conf import settings
@receiver(post_save, sender=Notification)
def my_call(sender,instance,created,**kwargs):
    if created:
        send_mail(subject=instance.title,message=instance.text,from_email=settings.EMAIL_HOST_USER,recipient_list=["tomazini@discente.ufg.br"])