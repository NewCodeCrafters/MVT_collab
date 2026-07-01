from django.db import models
from apps.user.models import User
from django.utils.text import slugify

CHOICE=(
    ("used","USED"),
    ("new","NEW"),
)

TYPE_CHOICE=(
    ("mid range","MID_RANGE"),
    ("low range","LOW_RANGE"),
    ("high range","HIGH_RANGE")
)

class Phone(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=100,choices=CHOICE, default='new')
    image = models.ImageField(upload_to='code images/')
    range = models.CharField(max_length=200,choices=TYPE_CHOICE, default='mid_range')
    create_at =models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.brand)
        super().save(*args, **kwargs)

