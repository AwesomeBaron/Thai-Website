from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('create-post/', views.create_post, name='create'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete'),
    path('<int:post_id>/edit-post/', views.edit_post, name='edit'),
    path('<int:post_id>/', views.post_detail, name='detail')

]