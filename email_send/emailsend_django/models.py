from django.db import models

# Create your models here.
class emailSend(models.Model):
    subject = models.CharField(max_length=20)
    body = models.CharField(max_length=20)
    image = models.FileField(upload_to='image/')