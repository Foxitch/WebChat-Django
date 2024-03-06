from django.contrib import admin

from chat.models import Chat, Contact, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
