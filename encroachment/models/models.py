from django.db import models
import uuid
from model_utils.fields import StatusField
from model_utils import Choices
from django import forms
from django.contrib.postgres.fields import ArrayField

# from rest_framework import serializers

# Create your models here.
class Encroachment_table(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    encrt_id=models.CharField(max_length=50)
    DEPARTMENT_CHOICES = (('Real Estate', "Real Estate"),
               ('Legal', "Legal"),
               ('Maintenance', "Maintenance"),
               ('Pipeline Integrity', "Pipeline Integrity"),
               ('Operation', "Operation"),
               ('Damage Prevention',"Damage Prevention"),
               ('Engineering',"Engineering"))
    department=ArrayField(
        models.CharField(
            choices=DEPARTMENT_CHOICES,
            max_length=100,
            blank=True,
            null=True
        ),
        blank=True,
        null=True
    )
    STATUS_CHOICES = Choices('active', 'assigned','follow_up','resolved','audited','rejected')
    status = StatusField(choices_name='STATUS_CHOICES')
    ENCRT_TYPE_CHOICES = (('Erosion', "Erosion"),
               ('Large trees', "Large trees"),
               ('Fences', "Fences"),
               ('Utility poles', "Utility poles"),
               ('Excavation', "Excavation"),
    )
    encrt_type=ArrayField(
        models.CharField(
            choices=ENCRT_TYPE_CHOICES,
            max_length=100,
            blank=True,
            null=True
        ),
        blank=True,
        null=True
    )
    region=models.CharField(max_length=50)
    subregion=models.CharField(max_length=50)
    encrt_size=models.FloatField()
    dist_coa=models.IntegerField()
    CRITICALITY_CHOICES = Choices('high', 'low')
    criticality=StatusField(choices_name='CRITICALITY_CHOICES')
    assigned_to =ArrayField(
        models.CharField(
            choices=DEPARTMENT_CHOICES,
            max_length=100,
            blank=True,
            null=True
        ),
        blank=True,
        null=True,
        help_text="Only required if 'assigned' is selected."
    )
    follow_up_by=models.FloatField(blank=True, null=True, help_text="Only required if 'follow_up' is selected.")
    resolved_by=ArrayField(
        models.CharField(
            choices=DEPARTMENT_CHOICES,
            max_length=100,
            blank=True,
            null=True
        ),
        blank=True,
        null=True,
        help_text="Only required if 'resolved' is selected."
    )
    audited_on=models.DateField(blank=True, null=True, help_text="Only required if 'audited' is selected.")
    reject_reason=models.CharField(max_length=500,blank=True, null=True, help_text="Only required if 'rejected' is selected.")


