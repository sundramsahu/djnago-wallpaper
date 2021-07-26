from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=False, blank=False)
    
    def __str__(self):
        return f'{self.id}'


    


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    id = models.AutoField(primary_key=True)


    def __str__(self):
        return f'{self.name}'


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    imgviiews = models.IntegerField(default=0)
    publish = models.BooleanField(default=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
