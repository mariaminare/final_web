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

]