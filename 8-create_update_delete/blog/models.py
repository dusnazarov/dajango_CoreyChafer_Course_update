from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse     

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):        
        return reverse('post-detail', kwargs={'pk': self.pk})




"""  
python manage.py shell
from django.contrib.auth.models import User
from blog.models import Post

user=User.objects.first()
user.save() 
post=Post(title="my first post", content="This is the content of my first post",author=user)
post.save()
post.author.username
post.author.email
posts_by_user = user.post_set.all()
created_post = user.post_set.create(title="my second post",content="second content") 

"""