from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from final_exam.posts.models import Post
from final_exam.threads.models import Comment

UserModel = get_user_model()


class Reaction(models.Model):
    REACTION_TYPES = (
        ('like', 'Like'),
        ('heart', 'Heart'),
        ('brain', 'Brain'),
    )
    reaction_type = models.CharField(max_length=20, choices=REACTION_TYPES)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not (bool(self.post) ^ bool(self.comment)):
            raise ValidationError("Either post or comment must be set, but not both.")
        super(Reaction, self).save(*args, **kwargs)
