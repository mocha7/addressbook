from django.conf.urls import url, include

from . import views
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='AddressBook API')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^delete/$', views.delete, name='delete'),
    #url(r'^api/addresses/$', views.api, name='api'),
    url(r'^api/', include(views.router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^swagger/$', schema_view)
]

