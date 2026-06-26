from django.db import models

TYPES = [
    ('user', 'User'),
    ('vendor', 'Vendor'),
    ('admin', 'Admin')
]

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200, choices=TYPES, default='user')
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

