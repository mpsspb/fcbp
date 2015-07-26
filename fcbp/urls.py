from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^api/v1/users/', include('users.urls')),
    # url(r'^$', 'fcbp.views.home', name='home'),
    url(r'^.*$', 'fcbp.views.home', name='home'),
)
