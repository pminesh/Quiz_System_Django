from CWH import views
from django.urls import path
urlpatterns = [
    path("index",views.index,name="index"),
    path("",views.loginUser,name="loginUser"),
    path("register",views.register,name="register"),
    path("contact",views.contact,name="contact"),
    path("logout",views.logoutuser,name="logoutuser"),
    path("<int:id>",views.take_quiz,name="take_quiz"),
]