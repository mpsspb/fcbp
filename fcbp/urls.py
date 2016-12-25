from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from finance.views import home, PaymentDateUpdate, PaymentAmountUpdate
from reports.views import Home as reports_home

urlpatterns = patterns(
    '',
    url(r'^api/v1/users/', include('users.urls')),
    url(r'^api/v1/products/', include('products.urls')),
    url(r'^api/v1/clients/', include('clients.urls')),
    url(r'^api/v1/employees/', include('employees.urls')),
    url(r'^api/v1/reports/', include('reports.urls')),
    url(r'^api/v1/finance/', include('finance.urls')),
    url(r'^finance/$', home.as_view(), name='finance'),
    url(r'^reports/$', reports_home.as_view(), name='reports'),
    url(r'finance/date/(?P<pk>[0-9]+)/$', PaymentDateUpdate.as_view(),
        name='payment-update-date'),
    url(r'finance/amount/(?P<pk>[0-9]+)/$', PaymentAmountUpdate.as_view(),
        name='payment-update-amount'),
    # url(r'^$', 'fcbp.views.home', name='home'),
)

if settings.DEBUG:
    # Server statics and uploaded media
    urlpatterns += static(settings.AVATAR_URL,
                          document_root=settings.AVATAR_ROOT)

urlpatterns += url(r'^.*$', 'fcbp.views.home', name='home'),
