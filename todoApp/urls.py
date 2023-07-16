from django.contrib import admin
from django.urls import path
from todoApp.views import home ,newTodo,login,signup,editTodo,deleteTodo,editTodoStatus, Logout,welcome

urlpatterns = [
    path('',welcome, name="welcome"),
    path('home/',home, name="home"),
    path('login/',login, name="login"),
    path('signup/',signup, name="signup"),
    path('post/new/',newTodo, name="newTodoList"),
    path('post/edit/<int:id>/',editTodo, name="editTodoList"),
    path('post/delete/<int:id>/',deleteTodo, name="deleteTodoList"),
    path('post/editStatus/<int:id>/<int:status>/',editTodoStatus, name="editTodoStatus"),
    path('logout/',Logout, name="logout"),
]