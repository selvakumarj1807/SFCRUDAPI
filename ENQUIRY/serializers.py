from rest_framework import serializers
from .models import StudentEnquiry

class StudentEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnquiry
        fields = '__all__'

    def validate_name(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Name is required.")
        return value

    def validate_dob(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Date of Birth is required.")
        return value

    def validate_mobile(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Mobile number is required.")
        
        student_id = self.instance.id if self.instance else None
        if StudentEnquiry.objects.filter(mobile=value).exclude(id=student_id).exists():
            raise serializers.ValidationError("Mobile number already exists.")
        return value

    def validate_email(self, value):
        if value:  # allow null or blank emails
            student_id = self.instance.id if self.instance else None
            if StudentEnquiry.objects.filter(email=value).exclude(id=student_id).exists():
                raise serializers.ValidationError("Email already exists.")
        return value

    def validate_education(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Education is required.")
        return value

    def validate_passout_year(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Pass-out year is required.")
        return value

    def validate_course(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Course is required.")
        return value
