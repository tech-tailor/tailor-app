from django.contrib import admin

from store.models import *



class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


    
    


admin.site.register(Tag, TagAdmin)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Carousel)
admin.site.register(Product)
