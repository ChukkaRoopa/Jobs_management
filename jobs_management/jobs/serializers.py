from rest_framework import serializers
from .models import Job
from django.core.exceptions import ValidationError

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
    
    def validate_years_of_experience(self, value):
        if value < 0:
            raise ValidationError("Years of experience cannot be negative.")
        return value