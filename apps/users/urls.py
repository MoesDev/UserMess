from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^user/login$', views.login, name="login"),
    url(r'^signout$', views.signout, name="signout"),
    url(r'^not_signed_in/$', views.not_signed_in, name="not_signed_in"),

    # User CRUD
    url(r'^user/show', views.show, name="show"),
    url(r'^user/new$', views.registrationPage, name="regPage"),
    url(r'^user/register$', views.register, name="register"),
    url(r'^user/edit/(?P<id>\d+)$', views.edit, name="edit"),
    url(r'^user/update/(?P<id>\d+)$', views.update, name="update"),
    url(r'^user/delete/(?P<id>\d+)/$', views.destroy, name="delete"),

]