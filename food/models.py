from django.db import models
from embed_video.fields import EmbedVideoField


class Food(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    image = models.FileField(blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']


class FoodImage(models.Model):
    post = models.ForeignKey(Food, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.post.title


class FoodVideo(models.Model):
    post = models.ForeignKey(Food, default=None, on_delete=models.CASCADE)
    video = EmbedVideoField()

    def __str__(self):
        return self.post.title