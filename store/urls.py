from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from store.converters import PhoneNumberConverter



urlpatterns = [
    path("", views.home, name="store_home"),
    path("product/", views.product, name="store_product"),
    path("accounts/profile/", views.myprofile, name="store_myprofile"),
    path("search/", views.searchpage, name="store_searchpage"),
    path("productpage/<uuid:product_id>/", views.productpage, name="store_productpage"), 
    path('accounts/', include('allauth.urls')),
   # path('work/', include('work.urls')),
   path('admin/', admin.site.urls),
   path("clients/<phone:phone_number>/", views.clientdetails, name="store_clientdetails"),
   path("accounts/nomeasurement/", views.no_measurement, name="store_no_measurement"),

]



if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
