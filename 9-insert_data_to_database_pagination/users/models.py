import django
from django.db import models
from django.contrib.auth.models import User
from PIL import Image   



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"
    

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/media/default.jpg'
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    
        img = Image.open(self.image.path)  
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)  

        # Additional image processing can be done here if needed
    

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