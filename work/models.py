from django.db import models
from django.contrib.auth.models import User
from .constants import TIME_CHOICES,EXPERIENCE
from offshift import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    
    def __str__(self):
        return self.name

class Work(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=6000)
    time = models.CharField(max_length=50, choices=TIME_CHOICES) 
    experience = models.CharField(max_length=50, choices=EXPERIENCE)
    category = models.ManyToManyField(Category)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client')
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='freelancer')
    budget = models.DecimalField(max_digits=12,decimal_places=2)
       
    def __str__(self) -> str:
        return f'{self.title}'
    
class Proposal(models.Model):
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='freelancer_proposal')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='client_proposal', null=True, blank=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    price = models.CharField(max_length=10,blank=True,null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Proposal by {self.freelancer.username} of {self.work.title}"