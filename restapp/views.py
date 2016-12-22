from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import MyModel
from .serializers import MyModelSerializer

@api_view(['GET','POST'])
def MyModelList(request):
	
	if request.method == 'GET':
		mymodel = MyModel.objects.all()
		serializer = MyModelSerializer(mymodel,many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = MyModelSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def MyModelDetail(request,pk):
	
	try:
		mymodel = MyModel.objects.get(pk=pk)
	except MyModel.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = MyModelSerializer(mymodel)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = MyModelSerializer(mymodel, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		mymodel.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)			








