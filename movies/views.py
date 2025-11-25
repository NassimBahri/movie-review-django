from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Film, Categorie


class HomePage(ListView):
    model = Film
    template_name = "index.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Categorie.objects.all()
        context["categories"] = categories
        return context


class CategoriePage(ListView):
    model = Film
    template_name = "categorie.html"

    def get_queryset(self):
        return Film.objects.filter(categorie=self.kwargs["id"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Categorie.objects.all()
        context["categories"] = categories
        context["categorie"] = Categorie.objects.get(pk=self.kwargs["id"])
        context["selected_page"] = "categorie"
        print(context["object_list"])
        return context

class MoviePage(DetailView):
    model = Film
    template_name = "details.html"
    context_object_name = "film"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Categorie.objects.all()
        context["categories"] = categories
        return context
    
    