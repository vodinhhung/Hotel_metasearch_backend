from rest_framework import serializers
from hotel.models import Domain, Root

class DomainSerializer(serializers.Serializer):
    index = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField()

    def create(self, validated_data):
        return Domain.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class RootSerializer(serializers.Serializer):
    index = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=500)
    address = serializers.CharField(max_length=500, allow_blank=False)
    logo = serializers.CharField(max_length=2083)
    lat = serializers.FloatField()
    long = serializers.FloatField()
    star = serializers.IntegerField()
    check_in = serializers.CharField(max_length=20, allow_blank=True)
    check_out = serializers.CharField(max_length=20, allow_blank=True)
    description = serializers.CharField(allow_blank=True)
    street = serializers.CharField(max_length=500, allow_blank=True)

    def create(self, validated_data):
        return Root.objects.create(**validated_data)