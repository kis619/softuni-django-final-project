from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Post(models.Model):
    MAX_TITLE_LENGTH = 200
    # MIN_CONTENT_LENGTH = 2000 #TODO: restore this
    MIN_CONTENT_LENGTH = 20
    MAX_CONTENT_LENGTH = 10000

    title = models.CharField(max_length=MAX_TITLE_LENGTH, blank=False)
    content = models.TextField(
        max_length=MAX_CONTENT_LENGTH,
        validators=[MinLengthValidator(MIN_CONTENT_LENGTH)],
        blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True,  db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
