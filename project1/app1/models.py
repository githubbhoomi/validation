from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     image=models.ImageField(upload_to='image',default=False)
#     class Meta:
#         db_table='auth_User'
    # def __str__(self):
    #     return self.first_name
    
    # def __str__(self):
# Create your models here.
class clients(models.Model):
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    client=models.CharField( max_length=150)
    logo=models.ImageField(upload_to='image',default=False)
    address=models.CharField(max_length=100)
    zip=models.IntegerField()
    dept=models.CharField(max_length=50)
    validation_no=models.CharField(max_length=6)
    def __str__(self):
        return self.client
    
