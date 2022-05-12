from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    text = models.TextField(max_length=140)
    pub_date = models.DateTimeField('date published', auto_now_add=True, db_index=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author_posts')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-pub_date',)


class Follow(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='follower')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='following')

    class Meta:

        constraints = [
            UniqueConstraint(fields=['author', 'user'], name='author')
        ]
