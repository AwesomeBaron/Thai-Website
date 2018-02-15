from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ('title', 'author', 'pub_date')
        list_filter = ('title')
