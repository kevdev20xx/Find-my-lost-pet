from django.urls import path

from . import views
app_name="find_my_lost_pet"
urlpatterns = [
    path("", views.index, name="index"),
    path("sign-up", views.sign_up,name="sign_up"),
    path("login", views.login,name="login")
]