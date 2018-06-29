from django.db import models

# Create your models here.
class Entry(models.Model):
    store_url = models.URLField(max_length=30)
    vid_url = models.URLField(max_length=30,unique=True)

    def __str__(self):
        return str(self.name)
