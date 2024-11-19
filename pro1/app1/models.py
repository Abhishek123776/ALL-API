from django.db import models

# Create your models here.

class Contact(models.Model):
    mobile_number=models.IntegerField()
    alternative_mobile_number=models.IntegerField()
    permanent_address=models.CharField(max_length=80)
    working_address=models.CharField(max_length=80)
    email=models.EmailField(max_length=50)

class Educationdetail(models.Model):
    emp_id=models.IntegerField()
    qualification=models.CharField(max_length=40)
    occupations=models.CharField(max_length=40)
    annual_income=models.FloatField()

class Familydetails(models.Model):
    father_name=models.CharField(max_length=40)
    mother_name=models.CharField(max_length=40)
    sister_name=models.CharField(max_length=40)
    about_family=models.CharField(max_length=80)

class Partnerprefarencedetails(models.Model):
    looking_for=models.CharField(max_length=40)
    caste=models.CharField(max_length=40)
    qualification=models.CharField(max_length=40)
    occupations=models.CharField(max_length=40)