from django.db import models

# Create your models here.
class Youtubecommment(models.Model):
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment
