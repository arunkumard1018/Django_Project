from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=75,blank=False,null=False)
    text = models.TextField(null=False,blank=False,default="")
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('Post-Detail', kwargs={'pk':self.pk})