from django.db import models
from django.core.exceptions import ValidationError

colors = (
    "#3e6958",
    "#60b48a",
    "#dfaf8f",
    "#9ab9d7",
    "#dc8cc4",
    "#8cd1d3",
    "#dcdccd",
    "#709080",
    "#AD0000",
    "#72D5A2",
    "#F0DFAF",
    "#94C0F3",
    "#EC93D5",
    "#93E1E3",
    "#EEEEEC",
)

class AlarmType(models.Model):
    name = models.CharField(max_length=35)
    wakeup = models.BooleanField()
    def_time = models.TimeField(null=True,blank=True)
    preptime_min = models.IntegerField()
    preptime_max = models.IntegerField()
    def __json__(self):
        return {
            "id":self.pk,
            "name":self.name,
            "wakeup":self.wakeup,
            "preptime_min":self.preptime_min,
            "preptime_max":self.preptime_max
        }
    def __unicode__(self):
        return self.name


class Alarm(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True,blank=True)
    type = models.ForeignKey(AlarmType)
    def clean(self):
        if self.time is None and ((self.type is None) or (self.type.def_time is None)):
            raise ValidationError('No time specified')
        if self.type is not None and self.type.wakeup and len(Alarm.objects.filter(date=self.date,type__wakeup=True).exclude(pk=self.pk)) > 0:
            raise ValidationError('Multiple wakeup alarms')

    def color(self):
        if self.type is not None:
            return colors[self.type.pk%len(colors)]
        else:
            return "#FFFFFF"

    def __json__(self):
        return {
            "id":self.pk,
            "date":self.date,
            "time":self.time,
            "type":self.type.pk
        }
    def get_time(self):
        if self.time:
            return self.time
        else:
            return self.type.def_time
    def is_wakeup(self):
        return self.type and self.type.wakeup

    def __unicode__(self):
        res = self.get_time().strftime("%H:%M")
        if self.type:
            res += " (%s)" % self.type
        return res
