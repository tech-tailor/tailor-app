from django.contrib import admin

from store.models import *


from django.conf import settings
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required




admin.site.login = staff_member_required(
    admin.site.login, login_url=settings.LOGIN_URL
)




class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Tag, TagAdmin)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Carousel)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(TemporaryPhoneNumber)
