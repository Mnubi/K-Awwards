from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('post/profile/', views.profile,name='profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('post/project/', views.post_project,name='project'),
    path('search/', views.search, name='search'),
    path('project/<int:project_id>/', views.project_details, name='project_details'),
    path('rate/<int:id>',views.rate, name='rate'),
]