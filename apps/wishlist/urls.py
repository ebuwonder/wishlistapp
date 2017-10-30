from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.main),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^authenticate$', views.authenticate),
    url(r'^logout$', views.logout),
    url(r'^additem$', views.additem),
	url(r'^additem/process$', views.additemprocess),
	url(r'^display/(?P<id>\d+)$', views.displayitem),
	url(r'^delete/(?P<id>\d+)$', views.deleteitem),
	url(r'^remove/(?P<id>\d+)$', views.removeitem),
	url(r'^addthis/(?P<id>\d+)$', views.addthis),
]
