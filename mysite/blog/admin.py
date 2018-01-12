from django.contrib import admin
from .models import Post

class PostAmin(admin.ModelAdmin):
    list_display = ('tilte','slug','author','publish','status')

admin.site.register(Post,PostAmin)
# Register your models here.
