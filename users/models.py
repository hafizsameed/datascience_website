from django.db import models
from django.contrib.auth.models import User
from competitions.models import Competitions
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    friends = models.ManyToManyField(User,related_name='friends')
    rated = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    participations = models.ManyToManyField(Competitions)

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def friend_list(self):
        return list(self.friends.all())

    @property
    def no_of_friend(self):
        return len(list(self.friends.all()))

    @property
    def comp_list(self):
        return list(self.participations.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img=Image.open(self.image.path)

        if img.height> 300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

