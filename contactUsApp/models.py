from django.db import models

# makemirations - Create changes and store in the file
# migrate - Apply the pending changes created by make migrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10) 
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    