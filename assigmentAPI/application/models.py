from django.db import models

# Create your models here.
# HelloWorld@2405

class WheelSpecification(models.Model):
    form_number = models.CharField(max_length=50, unique=True)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()
    fields = models.JSONField()

    def __str__(self):
        return self.form_number

