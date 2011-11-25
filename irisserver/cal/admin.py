from django.contrib import admin
from irisserver.cal.models import AlarmType,Alarm

class AlarmAdmin(admin.ModelAdmin):
    def change_view(self, request, *args,**kwargs):
        result = super(AlarmAdmin, self).change_view(request,*args,**kwargs)

        if not request.POST.has_key('_addanother') and not request.POST.has_key('_continue'):
            result['Location'] = "/cal/"
        return result
    def add_view(self, request, *args,**kwargs):
        result = super(AlarmAdmin, self).add_view(request,*args,**kwargs)

        if not request.POST.has_key('_addanother') and not request.POST.has_key('_continue'):
            result['Location'] = "/cal/"
        return result
    def delete_view(self, request, *args,**kwargs):
        result = super(AlarmAdmin, self).delete_view(request,*args,**kwargs)

        if not request.POST.has_key('_addanother') and not request.POST.has_key('_continue'):
            result['Location'] = "/cal/"
        return result

admin.site.register(AlarmType)
admin.site.register(Alarm,AlarmAdmin)

