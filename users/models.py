from django.db import models

# Create your models here.
class upload_image(models.Model):
    image = models.ImageField(upload_to='images/')