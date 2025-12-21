from django.urls import path
from .views import active_projects, proposals, contracts

urlpatterns = [
    path('projects/', active_projects),
    path('proposals/', proposals),
    path('contracts/', contracts),
]
