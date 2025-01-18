from rest_framework import serializers
from django.contrib.auth.models import User


class accpListSerializer(serializers.Serializer):
  accp = serializers.IntegerField()
  first_name = serializers.CharField(max_length=50)
  last_name = serializers.CharField(max_length=50)

class accpSaldoSerializer(serializers.Serializer):
  accp = serializers.IntegerField()
  date = serializers.DateField()
  summ = serializers.DecimalField(max_digits=10, decimal_places=2)


