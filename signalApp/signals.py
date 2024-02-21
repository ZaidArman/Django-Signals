from django.db.models.signals import pre_save, post_save # import pre and post save signals
from .models import Post, Profile
from django.contrib.auth.models import User
from django.dispatch import receiver, Signal

# def Post_Save(sender, instance, **kwargs):
#     print(' Post Save is Working')

# def Pre_Save(sender, instance, **kwargs):
#     print(' Pre Save is Working')

# post_save.connect(Post_Save, sender=Post)
# pre_save.connect(Pre_Save, sender=Post)

@receiver(post_save, sender=User) # we can also connect like this
def prof_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        print("Profile is created")
# post_save.connect(prof_created, sender=Post) # connect with signals



@receiver(post_save, sender=User) # we can also connect like this
def prof_updated(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.count += 1
        instance.profile.save()
        print("profile updated")
# post_save.connect(prof_updated, sender=Post)