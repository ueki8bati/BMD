from django.urls import path, include
from . import views,slack


app_name ='bookmarkd'

urlpatterns = [
    path('', slack.ReadMessage(), name='SlackRead'), 
    ]