from django.urls import path, re_path
from .views import HomePage, MoviePage, CategoriePage

urlpatterns = [
    path('', HomePage.as_view(), name="page_index"),
    re_path('movie/(?P<id>[0-9]+)', MoviePage.as_view(), name="page_details"),
    re_path('category/(?P<id>[0-9]+)', CategoriePage.as_view(), name="page_categories"),
]