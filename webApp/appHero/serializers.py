from rest_framework import serializers

from .models import Hero


class HeroSerializer(serializers.Serializer):
    hero_id = serializers.CharField(required=False, read_only=True)
    name = serializers.CharField()
    alias = serializers.CharField()
    email = serializers.CharField()


    def create(self, validated_data):
        return Hero.objects.create(**validated_data)

    def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.alias = validated_data.get('alias', instance.alias)
            instance.email = validated_data.get('email', instance.email)
            instance.save()
            return instance

