from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model =  Message
		fields = ('url', 'title', 'body', 'pub_date')