from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import ListCreateView, DetailAndUpdate

urlpatterns = [
    url(r'^movies/$', ListCreateView.as_view()),
    url(r'^movies/(?P<pk>[0-9]+)/',
        DetailAndUpdate.as_view())
]


urlpatterns = format_suffix_patterns(urlpatterns)