from django import forms
from .models import StudentEnquiry

class StudentEnquiryForm(forms.ModelForm):
    class Meta:
        model = StudentEnquiry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        
    
