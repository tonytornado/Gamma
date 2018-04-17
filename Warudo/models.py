from django.db import models

from Accounts.models import User
from Gamma import settings


class Cosplayer(models.Model):
    C_LEVEL = (
        ('N', 'Novice'),
        ('J', 'Journeyman'),
        ('M', 'Master'),
        ('P', 'Professional'),
    )

    EXPERTISE = (
        ('Needlework', 'Needle'),
        ('Armoring', 'Armor'),
        ('Makeup', 'MaUp'),
        ('Large Build', 'BigBuild'),
    )

    cosplayer_id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    identity = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='assets/img', null=True)
    focus = models.CharField(max_length=15, choices=EXPERTISE, null=True)
    lvl = models.CharField(max_length=20, choices=C_LEVEL, null=True)
    city = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.identity


class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    addressLine1 = models.CharField(max_length=140)
    addressLine2 = models.CharField(max_length=140, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.IntegerField


class Contest(models.Model):
    contest_id = models.IntegerField(primary_key=True)
    contest_name: models.CharField(max_length=200)
    placement1st: models.ForeignKey(Cosplayer, models.CASCADE, null=True)
    placement2nd: models.ForeignKey(Cosplayer, models.CASCADE, null=True)
    placement3rd: models.ForeignKey(Cosplayer, models.CASCADE, null=True)


class Convention(models.Model):
    convention_id = models.AutoField(primary_key=True)
    manager_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    competition = models.ForeignKey(Contest, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    profile_id = models.IntegerField(primary_key=True, auto_created=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    cosplayer = models.OneToOneField(Cosplayer, on_delete=models.CASCADE, blank=True)
    conventions = models.ManyToManyField(Convention, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return 'profile', (), {'pk': self.pk}

    def __str__(self):
        return self.user.username
