from django.db import models

class Employee_details(models.Model):
    WORK_TYPE_CHOICES = [
        ('contract', 'Contract'),
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
    ]

    employee_id = models.AutoField(primary_key=True) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    experience = models.PositiveIntegerField() 
    roles = models.CharField(max_length=50)
    work_type = models.CharField(max_length=30, choices=WORK_TYPE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position} ({self.get_roles_display()})"