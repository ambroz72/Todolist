from . import views
from django.urls import path

urlpatterns = [

    path('',views.add,name='add'),
    path('details/',views.details,name='details'),
    path('delete/<int:taskid>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')
]
