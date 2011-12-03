#http://djangosnippets.org/snippets/129/

from django import template
from cal.models import Alarm

register = template.Library()


import datetime

CALENDAR_LENGTH = 90

def calendar():
    today = datetime.date.today()
    start = today - datetime.timedelta(today.weekday())
    end = start + datetime.timedelta(CALENDAR_LENGTH)

    alarms = Alarm.objects.filter(date__gte=start,date__lt=end).order_by("date","time")
    alarm_i = 0

    month_cal = []
    week = []
    week_headers = []

    for i in range(CALENDAR_LENGTH):
        day = start + datetime.timedelta(i)
        if i < 7:
            week_headers.append(day)

        cal_day = {}
        cal_day['day'] = day

        cal_day['alarms'] = []
        while alarm_i < len(alarms) and alarms[alarm_i].date == day:
            if alarms[alarm_i].is_wakeup():
                cal_day["wakeup"] = alarms[alarm_i]
            cal_day['alarms'].append(alarms[alarm_i])
            alarm_i += 1

        week.append(cal_day)

        if day.weekday() == 6:
            month_cal.append(week)
            week = []

    return {'calendar': month_cal, 'headers': week_headers}

register.inclusion_tag('month.html')(calendar)


