from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class Tag(models.Model):
    caption = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=150)
    # image = models.ImageField(upload_to="images", null=True, blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField(Tag)
