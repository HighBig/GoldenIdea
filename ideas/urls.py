from django.conf.urls import url
from . import views


app_name = 'ideas.views'


urlpatterns = [
    url(r'^list/$',
        views.list_view,
        name='list'),
    url(r'^detail/(?P<idea_id>[0-9]+)/$',
        views.detail_view,
        name='detail'),
    url(r'^create/$',
        views.create_view,
        name='create'),
]
