from django.conf.urls import patterns, include, url

urlpatterns = patterns( 'indicadores.views',
	url(r'^insertar/$', 'insertar', name='insertar'),
    url(r'^$', 'indicadores', name='indicadores'),
)
