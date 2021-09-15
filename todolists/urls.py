from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('',views.index, name="index"),
    path('add', views.addTodoItem, name="add"),
    path('completed/<todo_id>', views.completedTodo, name="completed"),
    path('deletecompleted', views.deletecompleted, name="deletecompleted"),
    path('deleteall', views.deleteAll, name="deleteall")
]


urlpatterns += staticfiles_urlpatterns()