from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Custom fields for your user model
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='people')
    following = models.ManyToManyField('self', symmetrical=False, related_name='person')


    # Override the groups and user_permissions fields with custom related_name
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Customize the related_name
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Customize the related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )
