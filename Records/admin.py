from django.contrib import admin
from .models import NeckOpening, Record, PostImage
from . import views
#class RecordAdmin(admin.ModelAdmin):
#    list_display = ('id','Name', 'Phone')


#admin.site.register(NeckOpening)
#admin.site.register(Record, RecordAdmin)
#admin.site.register(PostImage)
#admin.site.site_url='/records/'

class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(Record)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    exclude=('Image', )
    list_display = ('Name', 'Phone', 'DateOfOrderTaken','DateOfDelivery')
    search_fields=('Name', 'DateOfDelivery')


    class Meta:
       model = Record
 
# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass

#admin.site.register(NeckOpening)
admin.site.site_url='/records/'
admin.site.site_header = 'Sefita Administration'