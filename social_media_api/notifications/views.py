# notifications/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notification
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def get_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(recipient=user).order_by('-timestamp')
    data = [
        {
            'actor': notification.actor.username,
            'verb': notification.verb,
            'target': str(notification.target),
            'timestamp': notification.timestamp,
            'read': notification.read,
        }
        for notification in notifications
    ]
    return Response(data)
