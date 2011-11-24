from cal.models import *
import utils

@utils.jsonview
def json(request):
    return {}

@utils.irisview
def index(request):
    return {}
