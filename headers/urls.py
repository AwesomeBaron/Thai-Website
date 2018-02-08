from django.conf.urls import url
from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('products/', views.products, name='products'),
    path('blog/', views.blog, name='blog'),
]
