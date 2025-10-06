from django.urls import path
from api.controllers.user import APILogin, APIRegister
from api.controllers.optical import OpticalController

urlpatterns = [
    path("register/", APIRegister.as_view(), name="register"),
    path("login/", APILogin.as_view(), name="login"),
    path("opticals/", OpticalController.as_view(), name="opticals"),
]
