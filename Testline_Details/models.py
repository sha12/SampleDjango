from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Testlines(models.Model):
     SBTS_ID=models.CharField(max_length=20,primary_key=True)
     Owner=models.CharField(max_length=50)
     Rack = models.CharField(max_length=50)
     Hw_config= models.CharField(max_length=200)
     Radio_modules = models.CharField(max_length=200, default="FXEB+FRGT+FXDB")
     SBTS_Build= models.CharField(max_length=200)
     Cell_Info = models.CharField(max_length=200)
     App_IP_Addr = models.CharField(max_length=200)
     Active_Alarms = models.CharField(max_length=200)
     Setup_config = models.CharField(max_length=200)
     Remote_ip = models.CharField(max_length=100,blank=True,null=True,default=None)
     Login_details = models.CharField(max_length=200,blank=True,null=True,default=None)
     L2_switch_ip= models.CharField(max_length=100,blank=True,null=True,default=None)
     Port = models.CharField(max_length=200,blank=True,null=True,default=None)
     UEs = models.CharField(max_length=200,default="to_be_added")
     IMSI = models.CharField(max_length=100,default="to_be_added")
     Calls = models.CharField(max_length=200)
     Issues_Investigations = models.CharField(max_length=200)
     #Investigations = models.CharField(max_length=200)
     Status_Comments = models.TextField()
     #lastmodifiedon = models.DateTimeField(default=None,null=True)
     lastmodifiedon = models.CharField(max_length=200)
     lastmodifiedby = models.CharField(max_length=100,null=True,blank=True,default=None)
     #slug= models.SlugField(unique=True)
     
     '''
     def save(self,*args,**kwargs):
         self.slug = slugify(self.SBTS_ID)
         super(Testlines,self).save(*args,**kwargs)
     '''
         
     class Meta:
         verbose_name_plural ="Testlines"
     def __str__(self):
         return self.SBTS_ID    

