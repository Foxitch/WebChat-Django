from django.urls import path

from chat_api.views import (ChatCreateView, ChatDeleteView, ChatDetailView,
                            ChatListView, ChatUpdateView)

app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view()),
    path('create/', ChatCreateView.as_view()),
    path('<pk>', ChatDetailView.as_view()),
    path('<pk>/update/', ChatUpdateView.as_view()),
    path('<pk>/delete/', ChatDeleteView.as_view())
]
