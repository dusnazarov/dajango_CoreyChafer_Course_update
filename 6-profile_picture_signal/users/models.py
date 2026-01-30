import django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"
    

"""python manage.py shell
from django.contrib.auth.models import User
from users.models import Profile
user = User.objects.filter(username='admin').first()
user.profile
user.profile.image
user.profile.image.url
user.profile.image.path
user.profile.image.delete()
user.profile.image.width
user.profile.image.height
exit()
"""