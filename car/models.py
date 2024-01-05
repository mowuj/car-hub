from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
# Create your models here.

class Car(models.Model):
    name=models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    price=models.IntegerField()
    quantity=models.IntegerField()
    description=models.TextField()
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='media/uploads')

    def __str__(self):
        return self.name