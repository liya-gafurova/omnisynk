from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    joined_at = serializers.SerializerMethodField()

    class Meta(object):
        model = User
        fields = ('id', 'email', 'joined_at', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def get_joined_at(self, instance) -> int:
        return int(instance.date_joined.timestamp())


class UserSigninRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserSigninResponseSerializer(serializers.Serializer):
    token = serializers.CharField(read_only=True)
