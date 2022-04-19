from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Address
from .serializers import AddressSerializer

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Search by Street': '/?category=category_name',
		'Search by City': '/?subcategory=category_name',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/item/pk/delete'
	}

	return Response(api_urls)
	
	
from rest_framework import serializers
from rest_framework import status
  
@api_view(['POST'])
def add_Address(request):
    address = AddressSerializer(data=request.data)
  
    # validating for already existing data
    if Address.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if address.is_valid():
        address.save()
        return Response(address.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_address(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        address = Address.objects.filter(**request.query_params.dict())
    else:
        address = Address.objects.all()
  
    # if there is something in items else raise error
    if address:
        dataa = AddressSerializer(address, many=True)
        return Response(dataa.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
		
		
@api_view(['POST'])
def update_address(request, pk):
    address = Address.objects.get(pk=pk)
    data = AddressSerializer(instance=address, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
		
		
@api_view(['DELETE'])
def delete_address(request, pk):
    address = get_object_or_404(Address, pk=pk)
    address.delete()
    return Response(status=status.HTTP_202_ACCEPTED)		