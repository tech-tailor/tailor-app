from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.home, name="store_home"),
    path("product/", views.product, name="store_product"),
    path("accounts/profile/", views.myprofile, name="store_myprofile"),
    path("search/", views.searchpage, name="store_searchpage"),
    path("productpage/<uuid:product_id>/", views.productpage, name="store_productpage"), 
]



if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
