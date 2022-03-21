from django.db import models
from django.db.models.fields import SlugField
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False,)    # O titulo de acordo com o modelo django deve ter 255 caracteres
    slug = SlugField(max_length=255, unique=True,)
    # www.meusite.com/blog/(slug)introdução-ao-django
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

