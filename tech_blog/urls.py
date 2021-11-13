from django.urls import path 
from . import views 

app_name = 'tech_blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='post-list'),
    path('detail/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('edit/<int:pk>', views.PostEdit.as_view(), name='post-edit'),
    path('delete/<int:pk>', views.PostDelete.as_view(), name='post-delete'),
    path('add/', views.PostAdd.as_view(), name='post-add'),
]
