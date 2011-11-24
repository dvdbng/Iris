from cal.models import *
from django.shortcuts import render_to_response
import utils

@utils.jsonview
def json(request):
    return {}


def index(request):
    return render_to_response("index.html",{})
