from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet

User = get_user_model()


class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_msgs', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.author.username

    @classmethod
    def last_10_messages(cls) -> QuerySet:
        return cls.objects.order_by('-created_at').all()[:10]
