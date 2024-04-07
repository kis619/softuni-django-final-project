from django.db import models

from final_exam.posts.models import UserModel, Post


class Comment(models.Model):
    MAX_CONTENT_LENGTH = 2000
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=MAX_CONTENT_LENGTH, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} commented on {self.post}'
