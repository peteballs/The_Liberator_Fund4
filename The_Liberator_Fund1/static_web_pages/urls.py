from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('ai_description', views.ai_description, name='ai_description'),
    path('results', views.results, name='results'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
]