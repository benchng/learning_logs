from django.urls import path
from . import views

app_name = "logs"

urlpatterns = [
    path('', views.index, name='index'),
    path('logs/', views.index, name='index'),
    path('topics/', views.topics, name='topics'), #added back the "S"
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),



]