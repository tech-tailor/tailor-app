from django.http import HttpResponse

from django.conf import settings
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required

admin.site.login = staff_member_required(
    admin.site.login, login_url=settings.LOGIN_URL
)