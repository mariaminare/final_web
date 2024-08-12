from django.urls import path
from . import views
urlpatterns = [
   path('',views.home, name='home'),
   path('about/',views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path('profile/<str:pk>/', views.profile, name='profile'),
   path('adding/<str:id>/', views.adding, name='adding'),
   path('delete/<str:id>/', views.delete, name='delete'),
   path('login/', views.login_page, name='login'),
   path('logout/', views.logout_page, name='logout'),
   path('register/', views.register_page, name='register'),
   path('add/', views.add_player, name='add'),
   path('delete_player/<str:id>/', views.delete_player, name='delete_player'),
   path('update_user/', views.update_user, name='update_user'),
   path('comment/<int:player_id>/', views.add_comment, name='add_comment'),
   path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
   path('drop/<str:id>/', views.drop, name='drop'),
]