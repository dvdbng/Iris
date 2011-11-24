from django.db import models
from django.core.exceptions import ValidationError

colors = (
    "#3e6958",
    "#705050",
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
    def_time = models.TimeField(null=True)
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


class Alarm(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    type = models.ForeignKey(AlarmType)
    def clean(self):
        if self.time is None and ((self.type is None) or (self.type.def_time is None)):
            raise ValidationError('No time specified')
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
