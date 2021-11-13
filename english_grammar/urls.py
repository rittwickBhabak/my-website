from django.urls import path 
from . import views 

app_name = 'english_grammar'

urlpatterns = [
    path('', views.ChapterList.as_view(), name='chapter-list'),
    path('detail/<int:pk>', views.ChapterDetail.as_view(), name='chapter-detail'),
    path('create/', views.AddChapter.as_view(), name='add-chapter'),
    path('edit/<int:pk>', views.UpdateChapter.as_view(), name='edit-chapter'),
    path('chapter/<int:chapter_id>/page/<int:page_no>', views.page_detail, name='page-detail'),
]
