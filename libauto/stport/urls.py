from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
#	path("login/",views.login,name = "student_login"),
	path("detail/",views.detail, name = "book detail"),
	path("register/", views.register, name = "student_register"),
	path("search/", views.search, name = "book_search"),
    path("rlogin/", views.rlogin, name = "login_rr"),

]
