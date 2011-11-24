from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
import json

def jsonview(view):
    def __inner__(request):
        try:
            res = (200,view(request))
        except Http404, e:
            res = (404,str(e))
        except Exception, e:
            res = (500,str(e))

        code,data = res

        httpres = HttpResponse(json.dumps({
            "status":code,
            "response": data,
        }),mimetype="application/json",status=code)

        httpres['Cache-Control'] = 'no-cache'

        return httpres

    return __inner__


def irisview(view):
    filename = "%s.html" % view.__name__
    def __inner__(request):
        ctx = view(request)
        return render_to_response(filename,context_instance=RequestContext(request,ctx))
    return __inner__

