from django.conf.urls import include, url
from rest_framework import routers
from druidapi.query.views.QueryView import QueryViewSet
from frontend import views

apirouter = routers.DefaultRouter()
apirouter.register(r'query', QueryViewSet)

urlpatterns = [
    url(r'^api/', include(apirouter.urls)),
    # TODO: drop these patterns into the specific app instead of including them here.
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.ResultsView.as_view(), name='results'),
    # Eh, I still like swagger a bit
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
