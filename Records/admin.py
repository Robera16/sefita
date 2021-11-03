from django.contrib import admin
from .models import NeckOpening, Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id','Name', 'Phone')


admin.site.register(NeckOpening)
admin.site.register(Record, RecordAdmin)
