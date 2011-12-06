from cal.models import *
import utils

@utils.jsonview
def json(request):
    return [x.__json__() for x in Alarm.objects.all()]

@utils.irisview
def index(request):
    return {}
