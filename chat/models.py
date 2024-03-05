from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet

User = get_user_model()


class Contact(models.Model):
    user = models.ForeignKey(to=User, related_name='friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    contact = models.ForeignKey(to=Contact, related_name='messages', on_delete=models.CASCADE, default=None)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.contact.user.username


class Chat(models.Model):
    participants = models.ManyToManyField(Contact, related_name='chat')
    messages = models.ManyToManyField(Message, blank=True)

    def last_10_messages(self) -> QuerySet:
        return self.messages.objects.order_by('-timestamp').all()[:10]

    def __str__(self):
        return str(self.pk)
