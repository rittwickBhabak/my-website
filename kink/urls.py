from django.urls import path 
from . import views 

app_name = 'kink'
urlpatterns = [
    path('', views.home, name='home-page'),
    path('<int:id>', views.video, name='video-page'),
    path('last-seen', views.last_seen, name="last-seen"),
    path('add-bookmark', views.bookmark, name="add-bookmark"),
    path('remove-bookmark', views.remove_bookmark, name="remove-bookmark"),
    path('update-bookmark', views.update_bookmark, name="update-bookmark"),
    path('update-raw-link', views.update_raw_link, name="update-raw-link"),
    path('update-mf-link', views.update_mf_link, name="update-mf-link"),
    path('bookmarks/<int:id>', views.bookmarks, name="bookmark-list"),
]
