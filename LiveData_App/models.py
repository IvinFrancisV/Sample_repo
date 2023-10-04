from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=255)
    country_description = models.TextField()
    country_flag = models.ImageField(upload_to = 'Flags')

    def __str__(self):
        return self.country_name
