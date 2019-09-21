from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Message
from .serializers import MessageSerializer

class MessageView(viewsets.ModelViewSet):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def wall(request):
	messages_list = Message.objects.order_by('-pub_date')
	context = {'messages_list': messages_list}
	return render(request, 'wall.html', context)

