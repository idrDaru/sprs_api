from rest_framework import serializers
from api.models.users import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'email': {"required": False, "allow_null": True},
            'password': {"required": False, "allow_null": True},
            'is_verified': {"required": False, "allow_null": True},
            'image_download_url': {"required": False, "allow_null": True},
            'type': {"required": False, "allow_null": True},
        }