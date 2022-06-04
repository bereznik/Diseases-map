from django.urls import path,re_path
from server import views

urlpatterns=[
    path('localidades', views.localidadesApi),
    re_path(r'localidades/(?P<pathId>[/\w]+)/$', views.localidadesApi),
    path('notificacoes', views.notificacoesApi),
    re_path(r'^notificacoes/(?P<pathId>[/\w]+)/$', views.notificacoesApi),
    path('notificacoes-total', views.notificacoesApi),
    re_path(r'^notificacoes-total/(?P<pathId>[/\w]+)/$', views.notificacoesApi),
    path('doencas', views.doencasApi),
    re_path(r'^doencas/(?P<pathId>[/\w]+)/$', views.doencasApi),
    path('usuarios', views.usuariosApi),
    re_path(r'^usuarios/(?P<pathId>[/\w]+)/$', views.usuariosApi)
]