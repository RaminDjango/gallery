from django.db import models

# Create your models here.


class InfoPictureAdd(models.Model):
    image         = models.FileField()
    title       = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)
    date        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.date}'   


    