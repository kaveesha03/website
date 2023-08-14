

# Create your models here.


from django.db import models
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Additional cleanup or operations before deleting the post
        super().delete(*args, **kwargs)
