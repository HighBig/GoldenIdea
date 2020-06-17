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
    url(r'^edit/$',
        views.edit_view,
        name='edit'),
    url(r'^export/$',
        views.export_view,
        name='export'),
    url(r'^accept/(?P<idea_id>[0-9]+)/$',
        views.accept_view,
        name='accept'),
]
