from django.db import models

class AlarmType(models.Model):
    name = models.CharField(max_length=35)
    wakeup = models.BooleanField()
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

    def __json__(self):
        return {
            "id":self.pk,
            "date":self.date,
            "time":self.time,
            "type":self.type.pk
        }
