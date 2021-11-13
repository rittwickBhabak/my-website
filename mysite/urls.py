from django.contrib import admin
from django.urls import path, include 
from . import views 

urlpatterns = [
    path('', views.HomeView.as_view(), name='home-page'),
    path('admin/', admin.site.urls),
    path('english_grammar/', include('english_grammar.urls')),
    path('restaurants/', include('restaurants.urls')),
    path('tech-blog/', include('tech_blog.urls')),
    path('choti-golpo/', include('choti_golpo.urls')),
    path('library/', include('library.urls')),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    # path('users/', include('app_users.urls')),
]
