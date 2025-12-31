from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # Définir les rôles possibles
    ROLE_CHOICES = (
        ('USER', 'Utilisateur'),
        ('PROMOTER', 'Promoteur'),
    )
    
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='USER')

    def is_promoter(self):
        return self.role == 'PROMOTER'

    def is_user(self):
        return self.role == 'USER'

    def __str__(self):
        return f"{self.username} ({self.role})"

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
