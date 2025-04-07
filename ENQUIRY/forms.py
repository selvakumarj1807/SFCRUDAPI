from django import forms
from .models import StudentEnquiry

class StudentEnquiryForm(forms.ModelForm):
    class Meta:
        model = StudentEnquiry
        exclude = ['enquiryId', 'created_at']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'placement': forms.Select(attrs={'class': 'form-control'}),
            'currently_working': forms.Select(attrs={'class': 'form-control'}),
            'profession': forms.Select(attrs={'class': 'form-control'}),
        }
