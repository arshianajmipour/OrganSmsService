from django.db import models

# Create your models here.

class State(models.Model):
    title = models.CharField(max_length=50,verbose_name = "state" )
    code = models.CharField(max_length=20,verbose_name = "state code" )


class City(models.Model):
    title = models.CharField( max_length=50 ,verbose_name = "city" )
    code = models.CharField( max_length=20 ,verbose_name = "city code" )
    state = models.ForeignKey(State, on_delete=models.CASCADE ,verbose_name = "state" )