from django.db import models

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=25)
    message = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True,blank=True)
    
    
    def __str__(self):
        return self.name
    
    
class Blogs(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(max_length=255)
    date = models.DateField(auto_now_add=True,blank=True)
    blog = models.TextField(max_length=5000)
    
    
    def __str__(self):
        return self.name
    
    

    

