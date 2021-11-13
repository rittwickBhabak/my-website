from django.http.request import validate_host
from django.urls import path 
from . import views 

app_name = 'choti_golpo'

urlpatterns = [
    path('', views.StoryList.as_view(), name='index'),
    path('create/', views.CreateStory.as_view(), name='create-story'),
    path('update/<int:pk>', views.UpdateStory.as_view(), name='update-story'),
    path('delete/<int:pk>', views.DeleteStory.as_view(), name='delete-story'),
    path('<int:pk>', views.StoryDetail.as_view(), name='detail-page'),
    path('add-talk', views.add_dirty_talk, name='add-talk'),
    path('talk-list/', views.DirtyTalkList.as_view(), name='talk-list'),
    path('delete-talk/<int:pk>', views.DeleteTalkView.as_view(), name='delete-talk'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
    path('online-upload', views.upload_online, name='online-upload'),
    path('story-completed', views.story_completed, name='story-completed'),
    path('edit-talk/', views.edit_talk, name='edit-talk'),
]
