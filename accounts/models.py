from django.db import models
from django.db.models.signals import post_save
from django.core.files.storage import default_storage as storage
from django.contrib.auth.models import User
from django.dispatch import receiver
from PIL import Image
# Create your models here.


class Profile(models.Model):
    '''This Profile model has a one to one relationship with the user that ensures only one profile can be uploaded per user'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg',
                              upload_to='profile_pics',
                              blank=True,
                              null=True)
    total_donated = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        '''Reducing image size then save in the local storage'''
        super(Profile, self).save(*args, **kwargs)

        if self.image:
            image = Image.open(self.image)
            size = (250, 250)
            format = "png"

            if image.height > 250 or image.width > 250:
                image.thumbnail(size, Image.ANTIALIAS)
                img = storage.open(self.image.name, "w")
                image.save(img, format)
                img.close()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''Creates a new user profile when a new user is registered'''
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    '''Saves profile when User is updated or changed'''
    instance.profile.save()