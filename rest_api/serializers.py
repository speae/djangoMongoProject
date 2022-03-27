from rest_framework import serializers
from .models import Addresses

# 실제로 넘겨줄 데이터 설정
class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ['name', 'phone_number', 'address']
