from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile, Watchlist


@receiver(post_save, sender=User)
def create_profile_watchlist(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Watchlist.objects.create(user=instance)




@receiver(post_save, sender=User)
def save_profile_watchlist(sender, instance, **kwargs):
    instance.profile.save()
    instance.watchlist.save()
