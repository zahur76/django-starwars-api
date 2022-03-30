from django.db import models


# Create your models here.
class Faction(models.Model):

    class Meta:
        verbose_name = "Faction"

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


# Create your models here.
class Character(models.Model):
    class Meta:
        verbose_name = "Character"

    faction = models.ForeignKey(
            'Faction', null=False, blank=False, on_delete=models.CASCADE,
            related_name='characters')
    name = models.CharField(max_length=254)
    GENDER = [
                ('Male', 'Male'),
                ('Female', 'Female'),
                ('Other', 'Other'), ]
    gender = models.CharField(max_length=6, choices=GENDER, null=False)
    birth_year = models.CharField(max_length=254)
    birth_planet = models.CharField(max_length=254)

    def __str__(self):
        return self.name
