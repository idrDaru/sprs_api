from rest_framework import serializers
from api.models.users import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'is_verified',
            'profile_file_name',
            'profile_file_path',
            'type',
            'created_at',
            'updated_at',
            'deleted_at',
        )