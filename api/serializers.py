from rest_framework import serializers
from .models import Person
import re

class PersonSerializer(serializers.ModelSerializer):

     id = serializers.IntegerField(read_only=True)
     name = serializers.CharField(max_length=100)
     def validate_name(self, value):
        #regex pattern to validate name
        name_pattern = re.compile(r'^[A-Za-z\s]+$') #this accomodate single or double names
        if not name_pattern.match(value):
            raise serializers.ValidationError("Please provide names in letters only")
        return value

     class Meta:
        model = Person
        fields = ['id', 'name']
