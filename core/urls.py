from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.myprofile, name="myprofile"),
    path("clients/", views.myclients, name="clients"),
    path("operation/", views.operation, name="operation"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("clients/<str:name>/<int:measurement_id>/", views.clientdetails, name="clientdetails"),
    path("jobs/<int:id>", views.jobdetails, name="jobdetails"),
]

if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)

