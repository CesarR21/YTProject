from django.urls import path

from . import views 

app_name = 'youtubecomments'
urlpatterns = [
    path('', views.index, name='index')
]