from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^api/v1/users/', include('users.urls')),
    url(r'^api/v1/products/', include('products.urls')),
    url(r'^api/v1/clients/', include('clients.urls')),
    # url(r'^$', 'fcbp.views.home', name='home'),
)

if settings.DEBUG:
    # Server statics and uploaded media
    urlpatterns += static(settings.AVATAR_URL,
                          document_root=settings.AVATAR_ROOT)

urlpatterns += url(r'^.*$', 'fcbp.views.home', name='home'),
