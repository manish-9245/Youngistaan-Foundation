from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
from django import forms

# Create your models here.
class Award(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(max_length=500,blank=True,null=True)
    def __str__(self):
        return self.name

class Volunteer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    #dob  = models.DateTimeField(blank=True,null=True)
    program_choices =[
        ("Bright Spark Education Program","Bright Spark Education Program"),
         ("Transformers (Livelihood)","Transformers (Livelihood)"),
         ("Feeding Program (Zero Hunger)","Feeding Program (Zero Hunger)"),
         ("Women of Courage (Gender)","Women of Courage (Gender)"),
         ("Youngistaan Animal Heroes","Youngistaan Animal Heroes"),
         ("Blood Donor","Blood Donor"),
         ("Others","Others"),
     ]
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    programs = MultiSelectField(choices=program_choices,null=True)
    awards = models.ManyToManyField(Award,null=True,blank=True)
    #social_instagram = models.CharField(max_length=100,null=True,blank = True)
    #social_facebook = models.CharField(max_length=100,null=True,blank = True)
    #social_linkedin = models.CharField(max_length=100,null=True,blank = True)
