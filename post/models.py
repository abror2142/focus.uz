from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Agenda(models.Model):
    title = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='posts', blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    region = models.ForeignKey(Region, blank=True, null=True, on_delete=models.DO_NOTHING)
    agenda = models.ForeignKey(Agenda, blank=True, null=True, on_delete=models.DO_NOTHING)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.user} {self.post.name} {self.rating}"


