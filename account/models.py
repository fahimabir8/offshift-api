from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client','client'),
        ('freelancer','freelancer'),
    )

    user_type = models.CharField(max_length=14, choices=USER_TYPE_CHOICES, default="freelancer")
    image = models.ImageField(upload_to = 'account/images/' ,null=True,blank=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    about_me = models.TextField(blank=True, null=True)

STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Review(models.Model):
    reviewer = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='client_reviewer')
    freelancer = models.ForeignKey(CustomUser, on_delete = models.CASCADE,related_name='freelancer_reviewee')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"Reviewer : {self.reviewer.first_name}      Reviewee: {self.freelancer.first_name}"