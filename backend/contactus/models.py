from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.TextField()
    email = models.TextField()
    subject = models.TextField(null=True)
    inquiryType = models.TextField()
    Message = models.TextField()
    