from django.db import models

# Create your models here.
class Entry(models.Model):
    store_url = models.URLField(max_length=30)
    template = models.CharField(max_length=10, default="basic")
    vid_url = models.URLField(max_length=100,unique=True)
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return str(self.store_url + " - " + self.template)
