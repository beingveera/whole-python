from django.db import models
 
class signup(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    dob=models.DateField()
    Email=models.EmailField()
    PassWord=models.CharField(max_length=20)
    CPassWord=models.CharField(max_length=20)

class login(models.Model):
    email=models.EmailField()
    passWord=models.CharField(max_length=20)

class contact(models.Model):
    mail=models.EmailField()
    text=models.TextField(max_length=100)

