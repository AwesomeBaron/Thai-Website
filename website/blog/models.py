from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

def upload_location(instance, filename):
    return "{}/{}".format(instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'post_id': self.pk})

    def __str__(self):
        return '{}'.format(self.title)
