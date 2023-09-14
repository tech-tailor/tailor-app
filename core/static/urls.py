from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name="core_home"),
    path("profile/", views.myprofile, name="core_myprofile"),
    path("client/", views.client, name="core_client"),
    path("operation/", views.operation, name="core_operation"),
    path("signin/", views.signin, name="core_signin"),
    path("signup/", views.signup, name="core_signup"),
    path("clients/<str:name>/<int:measurement_id>/", views.clientdetails, name="core_clientdetails"),
    path("jobs/<int:id>", views.jobdetails, name="core_jobdetails"),
]

if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)

