from django.db import models

# Create your models here.
class Person(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=255)
    p_address = models.CharField(max_length=255)
    p_med_issues = models.JSONField(default=list,blank=True)
    BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-'),
    ]
    p_blood_grp = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    p_phone = models.CharField(max_length=10)
    p_dob = models.DateField()
    p_gender = models.CharField(max_length=5,choices=[('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),])

    def __str__(self):
        return self.p_name

class Donation(models.Model):
    d_id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey(
        'Person',
        on_delete=models.CASCADE,
        to_field='p_id'
    )
    d_date = models.DateField()
    d_time = models.TimeField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"Donation {self.d_id} : {self.quantity}ml on {self.d_date}"

class Stock(models.Model):
    s_id = models.AutoField(primary_key=True)
    Blood_Group_Choices = [
        ('A+','A+'),('A-','A-'),
         ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    s_blood_group = models.CharField(max_length=3,choices=Blood_Group_Choices,unique=True)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.s_blood_group} - {self.quantity}ml"

class Receive(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_date = models.DateField()
    r_hospital = models.CharField(max_length=100)
    quantity = models.IntegerField()
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    p_id = models.ForeignKey('Person', on_delete=models.CASCADE, to_field='p_id')
    r_blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)

    def __str__(self):
        return f"{self.p_id.p_name} received {self.quantity}ml of {self.r_blood_group}"

