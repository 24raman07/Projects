from django.db.models import fields
from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = ['Street', 'City', 'State', 'Pincode', 'Country']


