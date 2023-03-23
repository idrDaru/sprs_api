from rest_framework import serializers
from api.models.parking_spots import ParkingSpot
from api.models.parking_layouts import ParkingLayout
from api.serializers.parking_layouts import ParkingLayoutSerializer

class ParkingLayoutRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        serializer = ParkingLayoutSerializer(value)
        return serializer.data
    
    def to_internal_value(self, data):
        try:
            layout = ParkingLayout.objects.get(id=data['id'])
            return layout
        except ParkingLayout.DoesNotExist:
            raise serializers.ValidationError(
                'Parking Layout Not Found'
            )

class ParkingSpotSerializer(serializers.ModelSerializer):
    layout = ParkingLayoutRelatedField(queryset=ParkingLayout.objects.all(), many=False)
    
    class Meta:
        model = ParkingSpot
        fields = (
            'id',
            'layout',
            'name',
            'type',
            'status',
            'position',
            'price'
        )
