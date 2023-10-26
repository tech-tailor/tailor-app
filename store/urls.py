from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from store.converters import PhoneNumberConverter



urlpatterns = [
    path("", views.home, name="store_home"),
    path("product/", views.product, name="store_product"),
    path("accounts/profile/<phone:phone_number>/", views.myprofile, name="store_myprofile"),
    path("accounts/profile2/", views.myprofile2, name="store_myprofile2"),
    path("search/", views.searchpage, name="store_searchpage"),
    path("productpage/<uuid:product_id>/", views.productpage, name="store_productpage"), 
    path('accounts/', include('allauth.urls')),
   # path('work/', include('work.urls')),
   path('admin/', admin.site.urls),
   path("neeyee-upload-measurement<phone:phone_number>/", views.clientdetails, name="store_clientdetails"),
   path("user-upload-measurement/<phone:phone_number>/", views.user_entered_measurement, name="store_user_entered_measurement"),
   path("accounts/nomeasurement/", views.no_measurement, name="store_no_measurement"),
   path("account/upload/", views.upload_measurement, name="store_upload_measurement"),

]



if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
