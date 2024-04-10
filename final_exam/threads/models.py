from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from final_exam.posts.models import Post

UserModel = get_user_model()


class Thread(models.Model):
    MAX_CONTENT_LENGTH = 2000
    MIN_CONTENT_LENGTH = 200
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(
        max_length=MAX_CONTENT_LENGTH,
        validators=[MinLengthValidator(MIN_CONTENT_LENGTH)],
        blank=False
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'Thread for {self.post} by {self.author}'


class Comment(models.Model):
    MAX_CONTENT_LENGTH = 2000
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField(max_length=MAX_CONTENT_LENGTH, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} commented on {self.thread.id}'
