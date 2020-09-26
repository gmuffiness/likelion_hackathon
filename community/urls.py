from django.urls import path, re_path
from . import views
from django.conf.urls import include

app_name = 'community'

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('<int:pk>/', views.post_detail, name = 'post_detail'),
    path('<int:pk>/edit', views.post_edit, name = 'post_edit'),
    path('<int:pk>/delete', views.post_delete, name = 'post_delete'),
    path('new/', views.post_new, name='post_new'),
]