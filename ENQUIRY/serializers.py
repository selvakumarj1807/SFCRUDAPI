from rest_framework import serializers
from .models import StudentEnquiry

class StudentEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnquiry
        fields = '__all__'