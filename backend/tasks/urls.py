from django.urls import path
from . import views

#Initiate endpoints
urlpatterns = [
    path("analyze/", views.analyze_tasks),
    path("suggest/", views.suggest_tasks),
]