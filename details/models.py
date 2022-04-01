from django.db import models


class Details(models.Model):
    name =         models.CharField(max_length=50)
    address =      models.CharField(max_length=100)
    phone =        models.IntegerField()
    image =        models.ImageField(upload_to='uploaded_image')


    def __str__(self):
        return self.name
    