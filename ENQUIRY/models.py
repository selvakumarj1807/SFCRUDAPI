from django.db import models

class StudentEnquiry(models.Model):
    enquiryId = models.CharField(max_length=10, unique=True, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.CharField(max_length=255, null=True, blank=True)  
    mobile = models.CharField(max_length=10, null=True, blank=True)  
    email = models.EmailField(null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    passout_year = models.CharField(max_length=4, null=True, blank=True)  
    course = models.CharField(max_length=255, null=True, blank=True)
    placement = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')], null=True, blank=True)
    currently_working = models.CharField(max_length=3, null=True, blank=True, choices=[('yes', 'Yes'), ('no', 'No')])
    profession = models.CharField(max_length=10, blank=True, null=True, choices=[('it', 'IT'), ('non-it', 'Non-IT')])
    company = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    pf = models.CharField(max_length=3, blank=True, null=True)
    uan = models.CharField(max_length=20, blank=True, null=True)
    form16 = models.CharField(max_length=3, blank=True, null=True, choices=[('yes', 'Yes'), ('no', 'No')])
    address = models.TextField(null=True, blank=True)
    pan_aadhar = models.CharField(max_length=20, null=True, blank=True)
    refer_by = models.CharField(max_length=255, null=True, blank=True)
    referer_mobile = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.enquiryId:
            last_entry = StudentEnquiry.objects.order_by('-id').first()
            new_number = int(last_entry.enquiryId[3:]) + 1 if last_entry else 1
            self.enquiryId = f"ENQ{new_number:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.enquiryId} - {self.name}"
