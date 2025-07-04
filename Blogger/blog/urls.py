from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup-page'),
    path('login/', views.loginn, name='login-page'),
    path('loginn/', views.loginn, name='login-page'),
    path('home/', views.home, name='home-page'),
    path('newpost/', views.newPost, name='new-post'),
    path('mypost/', views.myPost, name='my-post'),
    path('signout/', views.signout, name='signout-btn'),
    path('update/<int:post_id>/', views.updatePost, name='update-post'),
    path('delete/<int:post_id>/', views.deletePost, name='delete-post'),
]
