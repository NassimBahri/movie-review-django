from django.db import models


class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.titre


class Film(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=250)
    annee = models.IntegerField()
    duree = models.CharField(max_length=50)
    description = models.TextField()
    couverture = models.ImageField()
    favoris = models.IntegerField(default=0)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
