from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("workers/", views.workers, name="workers"),
    path("clients/", views.myclients, name="clients"),
    path("operation/", views.operation, name="operation"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("clients/<str:name>/", views.clientdetails, name="clientdetails"),
]