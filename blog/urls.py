from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>', views.post_show, name="post_show"),
    path('post/create', views.PostCreate.as_view(), name="post_create"),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),
    path('post/<int:pk>/update', views.PostUpdate.as_view(), name="post_update"),
    
]
