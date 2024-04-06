from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.templatetags.static import static

from final_exam import settings
from final_exam.accounts.managers import LetUsTalkUserManager


class LetUsTalkUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = LetUsTalkUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class LetUsTalkUserProfile(models.Model):
    FIRST_NAME_MAX_LENGTH = 42
    LAST_NAME_MAX_LENGTH = 42
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
    )
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, null=True, blank=True)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # TODO: img vs url field
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def get_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return static('images/default-avatar.jpg')

    def __str__(self):
        return f'{self.user.email} Profile'
