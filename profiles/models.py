from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# from django.contrib.sites.models import Site






class CustomUser(AbstractUser):
    # user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null = True)
    department = models.CharField(max_length = 255, null = True)


    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null = True)
    username = models.CharField(max_length=255, null = True)
    first_name = models.CharField(max_length=255, null = True)
    last_name = models.CharField(max_length=255, null = True)
    email = models.EmailField(max_length=255, null = True)
    photo = models.ImageField(blank=True, upload_to='photos')
    department = models.CharField(max_length = 255, null = True)
    city = models.CharField(max_length = 255, null = True)
    state = models.CharField(max_length = 255, null = True)
    mat_no = models.CharField(max_length = 255, null = True)
    graduation_year = models.DateField(null = True)
    study_year = models.DateField(null = True)
    department = models.CharField(max_length = 255, null = True)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"profile of {self.username}"
