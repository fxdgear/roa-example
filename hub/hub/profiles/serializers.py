from rest_framework import serializers

from profiles.models import DockerUser


class DockerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DockerUser


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = DockerUser
