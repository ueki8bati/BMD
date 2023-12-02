from django.urls import path, include
from . import views,slack


app_name ='bookmarkd'

urlpatterns = [
    #path('bookmark/',views.index,name='index'),
    path('bookmark/<int:id>/', views.detail, name='detail'),
    path('bookmark/add/',views.add,name='add'),
    #追記
    path('',views.index,name='index'),
    #path('bookmarks',views.BookmarksView.as_view(),name='list')
    #path('slack', slack.ReadMessage(), name='SlackRead'), 
    ]