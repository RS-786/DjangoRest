from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=64)
    age = serializers.IntegerField()
    hobby = serializers.CharField(max_length=64)

    def create(self,validated_data):
        return Person.objects.create(validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data('name',instance.name)
        instance.age = validated_data('age', instance.age)
        instance.hobby = validated_data('hobby', instance.hobb)
        instance.save()
        return instance
