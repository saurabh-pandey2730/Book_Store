from django.db import models
from django.core.validators import MinLengthValidator , MaxValueValidator
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinLengthValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=50)
    is_bestselling =  models.BooleanField()
    
    
    def __str__(self):
        return f"{self.title} ({self.rating})"
