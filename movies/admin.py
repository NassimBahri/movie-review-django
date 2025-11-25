from django.contrib import admin
from .models import Categorie, Film

class AdminCategorie(admin.ModelAdmin):
    ordering = ['titre']
    search_fields = ['titre']
    list_display = ['id', 'titre']

admin.site.register(Categorie, AdminCategorie)

class AdminFilm(admin.ModelAdmin):
    ordering = ['titre']
    search_fields = ['titre']
    list_display = ['couverture', 'titre', 'annee', 'categorie']

admin.site.register(Film, AdminFilm)