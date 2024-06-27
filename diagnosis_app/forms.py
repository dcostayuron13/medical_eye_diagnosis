from django import forms
from .models import UploadedImage, Report

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'patient_name', 
            'disease',
            'full_name', 
            'date_of_birth', 
            'gender', 
            'phone', 
            'email', 
            'report_date', 
            'reason_for_visit', 
            'diagnosis', 
            'treatment_plan', 
            'medications_prescribed', 
            'follow_up_instructions', 
            'next_steps', 
            'follow_up_appointment_schedule'
        ]