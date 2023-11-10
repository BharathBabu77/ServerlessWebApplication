from django.db import models

class EmployeeProfile(models.Model):
    empId = models.CharField(max_length=50, primary_key=True)
    empAge = models.IntegerField()
    empFirstName = models.CharField(max_length=50)
    empLastName = models.CharField(max_length=50)
