from rest_framework import serializers
from .models import Person
import re

class PersonSerializer(serializers.ModelSerializer):
     def validate_name(self, value):
        #regex pattern to validate name
        name_pattern = re.compile(r'^[A-Za-z\s]+ [A-Za-z\s]+$')
        if not name_pattern.match(value):
            raise serializers.ValidationError("Please provide full names in letters only")
        return value

     class Meta:
        model = Person
        fields = ['id', 'name']
