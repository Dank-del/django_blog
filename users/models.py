from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to="profile_pics")
    bio = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return f"{self.user.username} Profile"
    
