from django.urls import path
from rango import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('trading/', views.ivailo_pavlov, name='ivailop')
]

urlpatterns += staticfiles_urlpatterns()