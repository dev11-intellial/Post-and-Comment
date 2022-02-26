from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    pin = models.CharField(max_length =10)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post_message = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    like = models.IntegerField(default=0)


