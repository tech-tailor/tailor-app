from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'work'  #namespace for the work app

urlpatterns = [
    path("jobs/", views.jobs, name="work_jobs"),
    path("", views.home, name="work_home"),
    path("client/", views.client, name="work_client"),
    path("accounts/profile/", views.myprofile, name="work_myprofile"),
    path("operation/", views.operation, name="work_operation"),
    path("clients/<str:measurement_name>/", views.clientdetails, name="work_clientdetails"),
    path("available-jobs/<str:job_name>/", views.jobdetails, name="work_jobdetails"),
    path("client-measurement/<str:measurement_name>/", views.clientmeasurement, name="work_clientmeasurement"),
    path("perror_log/", views.error_log, name="work_error_log"),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    #path('store/', include('store.urls')),
    path("worker-form/", views.worker_form, name="work_worker_form"),
]   


if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)

