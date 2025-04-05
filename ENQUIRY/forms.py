# ENQUIRY/forms.py
from django import forms
from .models import StudentEnquiry

class StudentEnquiryForm(forms.ModelForm):
    class Meta:
        model = StudentEnquiry
        exclude = ['enquiryId', 'created_at']
