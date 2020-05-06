from django.conf.urls import url
from . import views


app_name = 'accounts.views'


urlpatterns = [
    url(r'^login/$',
        views.login_view,
        name='login'),
    url(r'^ajax_login/$',
        views.ajax_login_view,
        name='ajax-login'),
    url(r'^logout/$',
        views.logout_view,
        name='logout'),
    url(r'^change_password/$',
        views.change_password_view,
        name='change-password'),
]
