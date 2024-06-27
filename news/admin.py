from django.contrib import admin
from .models import NewsPost, Category

# Register your models here.
admin.site.register(NewsPost)
admin.site.register(Category)
