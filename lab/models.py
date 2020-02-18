from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db import models
from django.contrib.sessions.models import Session
# Create your models here.

class UserSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.OneToOneField(Session,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Test(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
        
    
class Subtest(models.Model):
    name = models.CharField(max_length=100)
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='subtest',blank=True, null=True)
    unit = models.CharField(max_length=10)
    reference_value = models.IntegerField()
    selected = models.BooleanField(default=False)
    def __str__(self):
        return self.name

        

# class Doctor(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name


class Patient(models.Model):
    GENDER = (("0","M"),("1","F"))
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER,max_length=2)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("create_form", kwargs={"pk": self.pk})
    