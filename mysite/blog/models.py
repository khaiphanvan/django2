from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Post(models.Model):
    STATUS_CHOISE = (
        ('draft','Draft'),
        ('published','Published'),
    )

    tilte = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_post',on_delete=models.SET(get_sentinel_user))
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOISE,default='draft')
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.tilte

# Create your models here.
