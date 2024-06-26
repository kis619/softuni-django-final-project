from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()


class Post(models.Model):
    MAX_TITLE_LENGTH = 200
    MIN_CONTENT_LENGTH = 2000
    MAX_CONTENT_LENGTH = 10000

    title = models.CharField(max_length=MAX_TITLE_LENGTH, blank=False)
    content = models.TextField(
        max_length=MAX_CONTENT_LENGTH,
        validators=[MinLengthValidator(MIN_CONTENT_LENGTH)],
        blank=False,
    )
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
