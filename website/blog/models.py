from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def upload_location(instance, filename):
    return "{}/{}".format(instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    image = models.ImageField(upload_to=upload_location)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'titile is {}'.format(self.title)
