from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('post/profile/', views.profile,name='profile'),
    path('update_profile/<int:id>',views.update_profile, name='update_profile'),
    path('post/',views.post_project,name='post_project'),
    path('search/', views.search, name='search'),

]