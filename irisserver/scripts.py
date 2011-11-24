from irisserver.cal.models import AlarmType,Alarm
import datetime

def populate_cal():
    i = datetime.date(2011,11,24)
    delta = datetime.timedelta(1)
    weekend = AlarmType.objects.get(pk=1)
    unia = AlarmType.objects.get(pk=2)
    unib = AlarmType.objects.get(pk=3)

    for j in range(90):
        type = {
            1:unia,
            2:unib,
            3:unib,
            4:unia,
            5:weekend,
            6:weekend,
            7:weekend,
        }[i.isoweekday()]

        a = Alarm(date=i,time=None,type=type)
        a.save()
        i = i+delta
