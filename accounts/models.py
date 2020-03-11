from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    '''This Profile model has a one to one relationship with the user that ensures only one profile can be uploaded per user'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_donated = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s profile"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''Creates a new user profile when a new user is registered'''
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    '''Saves profile when User is updated or changed'''
    instance.profile.save()
