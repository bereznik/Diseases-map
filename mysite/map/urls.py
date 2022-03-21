from . import views
from django.urls import include, path


urlpatterns = [
    path('teste/',views.map,name = 'map')
]