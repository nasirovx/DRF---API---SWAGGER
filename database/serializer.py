from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Person
        fields = '__all__'