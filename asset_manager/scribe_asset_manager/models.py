from django.db import models


class ScribeAssetManager(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    image = models.ImageField(null=True)


    class Meta:
        ordering = ['-created']