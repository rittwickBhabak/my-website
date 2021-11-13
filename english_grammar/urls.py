from django.urls import path 
from . import views 

app_name = 'english_grammar'

urlpatterns = [
    path('', views.ChapterList.as_view(), name='chapter-list'),
    path('detail/<int:pk>', views.ChapterDetail, name='chapter-detail'),
    path('create/', views.AddChapter.as_view(), name='add-chapter'),
    path('update/<int:pk>', views.UpdateChapter.as_view(), name='chapter-update'),
    path('page/<int:pk>', views.PageDetail.as_view(), name='page-detail'),
]
