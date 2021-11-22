from django.db import models
import uuid

class Image(models.Model):
    title = models.CharField(max_length=200, default=uuid.uuid4)
    image = models.ImageField(blank=False, upload_to='images/')
    
    def __str__(self):
        return self.title
 
 