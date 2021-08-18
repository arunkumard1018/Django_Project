from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('',PostListView.as_view(),name='home'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'user/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name = 'user/logout.html'),name='logout'),
    path('profile',views.profile,name='profile'),
    path('post/<int:pk>',PostDetailView.as_view(),name='Post-Detail'),
    path('post/new/', PostCreateView.as_view(), name='Post-Create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name="Post-Update"),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name="Post-Delete"),
]