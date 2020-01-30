from django.db import models
# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    # def __str__(self):
    #     return self.title
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField()
    contactNo = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
   

