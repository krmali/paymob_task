from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User

class MessageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model =  Message
		fields = ('url', 'title', 'body', 'pub_date', 'author')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	messages = MessageSerializer(many=True, read_only=True)
	# messages = serializers.StringRelatedField(many=True)

	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'email', 'messages')