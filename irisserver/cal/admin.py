from django.contrib import admin
from irisserver.cal.models import AlarmType,Alarm

admin.site.register(AlarmType)
admin.site.register(Alarm)

