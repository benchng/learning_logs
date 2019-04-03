from django.urls import path, include
from . import views

app_name = "logs"

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', include('users.urls')),
    path('logs/', views.index, name='index'),
    path('topics/', views.topics, name='topics'), #added back the "S"
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')

]