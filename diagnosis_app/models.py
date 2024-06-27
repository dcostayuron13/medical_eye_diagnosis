
from django.db import models


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploaded_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Prediction(models.Model):
    image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    predicted_class = models.CharField(max_length=100)
    confidence = models.FloatField()
    predicted_at = models.DateTimeField(auto_now_add=True)


class Report(models.Model):
    patient_name = models.CharField(max_length=200)
    disease = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    report_date = models.DateField()
    reason_for_visit = models.CharField(max_length=200)
    diagnosis = models.CharField(max_length=200)
    treatment_plan = models.CharField(max_length=200)
    medications_prescribed = models.CharField(max_length=200)
    follow_up_instructions = models.CharField(max_length=200)
    next_steps = models.CharField(max_length=200)
    follow_up_appointment_schedule = models.DateTimeField()

    def __str__(self):
        return self.patient_name