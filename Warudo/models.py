from django.db import models

from Accounts.models import User


class LocalCity(models.Model):
    city = models.CharField(max_length=20)

    def __str__(self):
        return self.city


class LocalState(models.Model):
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.state


class Convention(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(LocalCity, models.CASCADE, related_name="ConventionCity")
    state = models.ForeignKey(LocalState, models.CASCADE, related_name="ConventionState")
    competition = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Cosplayer(models.Model):
    C_LEVEL = (
        ('N', 'Novice'),
        ('J', 'Journeyman'),
        ('M', 'Master'),
        ('P', 'Professional'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Identity = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='assets/img')
    city = models.ForeignKey(LocalCity, models.CASCADE, related_name="CosplayerCity")
    state = models.ForeignKey(LocalState, models.CASCADE, related_name="CosplayerState")
    lvl = models.CharField(max_length=20, choices=C_LEVEL)
    compete = models.ManyToManyField(Convention)

    def __str__(self):
        return self.Identity


class Profile(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    cosplayer = models.OneToOneField(Cosplayer, models.CASCADE, primary_key=False)
    conventions = models.ManyToManyField(Convention)

    @models.permalink
    def get_absolute_url(self):
        return 'profile', (), {'pk': self.pk}

    def cos_location(self):
        return "{}, {}".format(self.cosplayer.city, self.cosplayer.state)

    def __str__(self):
        return self.user.username
