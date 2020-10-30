from rest_framework import serializers 
from hotel.models import Province, Root, Url
 
class HotelSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Root
        fields = ('id',
                  'name',
                  'star',
                  'logo',
                  'address')


from rest_framework import serializers
from hotel.models import Domain, Root

class RootSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=500)
    address = serializers.CharField(max_length=500, allow_blank=False)
    logo = serializers.CharField(max_length=2083)
    star = serializers.IntegerField()

    def create(self, validated_data):
        return Root.objects.create(**validated_data)