from .models import MyModel

from rest_framework import serializers

class MyModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = MyModel
		fields = ('id','title','desc')

