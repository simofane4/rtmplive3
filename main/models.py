from django.db import models

# Create your models here.

class Secteurs(models.Model):
    name_sec = models.CharField(max_length=250)
    def __str__(self):
        return self.name_sec

class SouSecteurs(models.Model):
    secteur = models.ForeignKey(Secteurs , on_delete=models.CASCADE) 
    name_s_sec = models.CharField(max_length=200)
    def __str__(self):
        return self.name_s_sec

class Site(models.Model):
    s_sec = models.ForeignKey(SouSecteurs,on_delete=models.CASCADE)
    name_site = models.CharField(max_length=250)
    def __str__(self):
        return self.name_site

class Camera(models.Model):
    site = models.ForeignKey(Site,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    def __str__(self):
        return self.name  



    
