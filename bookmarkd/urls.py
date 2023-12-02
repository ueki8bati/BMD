from django.urls import path, include
from . import views,slack


app_name ='bookmarkd'

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('bookmark/',views.Index.as_view(),name='index'),
    path('bookmark/<int:id>/', views.detail, name='detail'),
    path('bookmark/add/',views.add,name='add'),
    #追記
    path('bookmark/<int:id>/edit/', views.edit, name='edit'),
    path('bookmark/<int:id>/delete/', views.delete, name='delete'),
    #path('bookmarks',views.BookmarksView.as_view(),name='list')
    #path('slack', slack.ReadMessage(), name='SlackRead'), 
    ]