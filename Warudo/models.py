from django.db import models

from Accounts.models import User


class Address(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    StreetName = models.CharField(max_length=100)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    ZipCode = models.IntegerField()


class Cosplayer(models.Model):
    NA = 'GA'
    CRAFT = 'Cr'
    NEEDLE = 'Ne'
    ARMOR = 'Ar'
    PROP = 'Pr'
    EXPERT_FOCUS = (
        (NA, 'General'),
        (CRAFT, 'Craftsmanship'),
        (NEEDLE, 'Needlework'),
        (ARMOR, 'Armorer'),
        (PROP, 'Prop-Master')
    )

    user = models.OneToOneField(User, models.CASCADE)
    Name = models.CharField(max_length=50)
    Expertise = models.CharField(choices=EXPERT_FOCUS, default=NA, max_length=10)
    CosUrl1 = models.URLField(max_length=100)
    CosUrl2 = models.URLField(max_length=100)
    CosUrl3 = models.URLField(max_length=100)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return "%s" % self.Name

    def get_absolute_url(self):
        return 'cos-profile', (), {'slug': self.slug}


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True)
    cosplayer = models.OneToOneField(Cosplayer, models.CASCADE)
    address = models.OneToOneField(Address, models.CASCADE)
    LikeCount = models.IntegerField(default=0)
