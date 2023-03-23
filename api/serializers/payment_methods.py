from rest_framework import serializers
from api.models.payment_methods import PaymentMethod
from api.models.parking_users import ParkingUser
from api.serializers.parking_users import ParkingUserSerializer

class ParkingUserRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        serializer = ParkingUserSerializer(value)
        return serializer.data
    
    def to_internal_value(self, data):
        try:
            user = ParkingUser.objects.get(id=data['id'])
            return user
        except ParkingUser.DoesNotExist:
            raise serializers.ValidationError(
                'User Not Found'
            )

class PaymentMethodSerializer(serializers.ModelSerializer):
    user = ParkingUserRelatedField(queryset=ParkingUser.objects.all(), many=False)
    class Meta:
        model = PaymentMethod
        fields = (
            'id',
            'user',
            'card_number',
            'expires_year',
            'expires_month',
            'cvv',
            'type',
            'email',
        )