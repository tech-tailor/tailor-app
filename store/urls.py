from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse


urlpatterns = [
    path("", views.home, name="store_home"),
    path("product/", views.product, name="store_product"),
    path("login/", views.login, name="store_login"),
    path("logout/", views.logout, name="store_logout"),
    path("register/", views.register, name="store_register"),
    path("error404/", views.error404, name="store_error404"), 
    path("search/", views.searchpage, name="store_searchpage"),
    path("productpage/", views.productpage, name="store_productpage"), 
]



if settings.DEBUG:
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
