from django.db import models

# Create your models here.
class register(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()
    role = models.CharField(max_length=100)
    Password = models.CharField(max_length=10)
    C_Password = models.CharField(max_length=10)

class Add_patientdetails(models.Model):
    Date = models.DateTimeField( auto_now=False, auto_now_add=False)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    CHOICES =[
        ('male','male'),
        ('female','female')
    ]
    Gender = models.CharField(max_length=10,choices=CHOICES,null= False,blank=False)
    Occupation = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Contactno = models.IntegerField()
    Chief_complaint = models.CharField(max_length=100)
    Injury = models.CharField(max_length=100)
    History = models.CharField(max_length=100)
    Pain = models.CharField(max_length=100)
    Site = models.CharField(max_length=100) 
   
    Duration = models.TimeField() 
    Onset = models.CharField(max_length=100)
    A_factor = models.CharField(max_length=100)
    R_factor = models.CharField(max_length=100)
    On_palpation = models.CharField(max_length=100)
    Special_test = models.CharField(max_length=100)
    Treatment = models.CharField(max_length=100)

