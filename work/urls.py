from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name="work_home"),
    path("profile/", views.myprofile, name="work_myprofile"),
    path("client/", views.client, name="work_client"),
    path("operation/", views.operation, name="work_operation"),
    path("signin/", views.signin, name="work_signin"),
    path("signup/", views.signup, name="work_signup"),
    path("clients/<str:name>/<int:measurement_id>/", views.clientdetails, name="work_clientdetails"),
    path("jobs/<int:id>", views.jobdetails, name="work_jobdetails"),
    path("perror_log/", views.error_log, name="work_error_log"),
]   


if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)

