from django.urls import path,re_path
from server import views

urlpatterns=[
    path('doencas', views.doencasApi),
    re_path(r'^doencas/(?P<pathId>[/\w]+)/$', views.doencasApi)
]