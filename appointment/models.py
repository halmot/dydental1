from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    wcode = models.CharField(max_length=8)
    name = models.CharField(max_length=20)
    birthday = models.DateTimeField()
    nationality = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICE = (
        (MALE, '男'),
        (FEMALE, '女')
    )
    sex = models.CharField(
        max_length=5,
        choices=GENDER_CHOICE,
        default=MALE,
    )
    cellphone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)


class HealthStatus(models.Model):
    drug_allergy = models.CharField(max_length=100)
    food_allergy = models.CharField(max_length=100)
    other_allergy = models.CharField(max_length=100)
    is_heart_disease = models.NullBooleanField
    is_pacemaker = models.NullBooleanField
    is_hypertension = models.NullBooleanField
    is_diabetes = models.NullBooleanField
    is_hepatitis = models.NullBooleanField
    is_Hbsag = models.NullBooleanField
    is_AIDS = models.NullBooleanField
    other_infectious_diseases = models.CharField(max_length=100)
    is_smoke = models.NullBooleanField




