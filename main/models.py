from django.db import models

# Create your models here.


class Recommendation(models.Model):
    name = models.CharField(max_length=255, null=True)
    category = models.ForeignKey('main.Category', null=True)
    info = models.TextField(null=True)
    address = models.TextField(null=True, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=150, blank=True)
    email = models.CharField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    twitter = models.CharField(max_length=150, blank=True)
    facebook = models.CharField(max_length=150, blank=True)
    youtube = models.CharField(max_length=500, blank=True)
    map_img = models.ImageField(upload_to='maps', blank=True)
    image1 = models.ImageField(upload_to='recommendations', blank=True)
    image2 = models.ImageField(upload_to='recommendations', blank=True)
    image3 = models.ImageField(upload_to='recommendations', blank=True)
    image4 = models.ImageField(upload_to='recommendations', blank=True)
    image5 = models.ImageField(upload_to='recommendations', blank=True)
    image6 = models.ImageField(upload_to='recommendations', blank=True)
    image7 = models.ImageField(upload_to='recommendations', blank=True)
    image8 = models.ImageField(upload_to='recommendations', blank=True)
    image9 = models.ImageField(upload_to='recommendations', blank=True)
    image10 = models.ImageField(upload_to='recommendations', blank=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    info = models.TextField(null=True)

    def __unicode__(self):
        return self.name
