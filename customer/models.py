from django.db import models
from car.models import Car
# Create your models here.

class Comment(models.Model):
    name=models.CharField(max_length=50)
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name='comments')
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name