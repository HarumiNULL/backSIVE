from django.urls import path
from api.controllers.user import APILogin, APIRegister
from api.controllers.optical import OpticalController
from api.controllers.optical import OpticalController, DayController, HourController, ScheduleController

urlpatterns = [
    path("register/", APIRegister.as_view(), name="register"),
    path("login/", APILogin.as_view(), name="login"),
    path("opticals/", OpticalController.as_view(), name="opticals"),
    
        # 🕒 rutas para el módulo horario
    path("days/", DayController.as_view(), name="days"),
    path("hours/", HourController.as_view(), name="hours"),
    path("schedules/", ScheduleController.as_view(), name="schedules"),
    #path("schedules/<int:pk>/", ScheduleController.as_view(), name="schedule_detail"),
]
