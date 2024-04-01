from django.db.models.signals import post_save
from django.dispatch import receiver

from final_exam.accounts.models import LetUsTalkUser, LetUsTalkUserProfile


@receiver(post_save, sender=LetUsTalkUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        LetUsTalkUserProfile.objects.create(user=instance)
