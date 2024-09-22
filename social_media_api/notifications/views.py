from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.response import Response

# Create your views here.

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

class MarkNotificationReadView(generics.UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        notification = self.get_object()
        if notification.recipient != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        notification.is_read = True
        notification.save()
        return Response({'status': 'notification marked as read'})