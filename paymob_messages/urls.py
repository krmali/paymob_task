from django.urls import path, include, re_path
from . import views
from rest_framework import routers
from django.views.generic.base import TemplateView

router = routers.DefaultRouter()
router.register('messages', views.MessageView)

urlpatterns = [
	# path('', TemplateView.as_view(template_name='home.html'), name='home'),
	path('', views.wall, name='wall'),
	path('signup/', views.signup, name='signup'),
	re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
	path('new_msg/', views.new_msg, name='new_msg'),
	path('', include('django.contrib.auth.urls')),
	path('api/', include(router.urls))
]
