from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url("^\.json$","cal.views.json",name="calendar_json"),
    url("^$","cal.views.index",name="calendar"),
)
