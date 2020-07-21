from django.conf.urls import url
from . import views


app_name = 'activities.views'


urlpatterns = [
    url(r'^list/$',
        views.list_view,
        name='list'),
    url(r'^detail/(?P<activity_id>[0-9]+)/$',
        views.detail_view,
        name='detail'),
    url(r'^create/$',
        views.create_view,
        name='create'),
    url(r'^vote/$',
        views.vote_view,
        name='vote'),
    url(r'^edit/$',
        views.edit_view,
        name='edit'),
]
