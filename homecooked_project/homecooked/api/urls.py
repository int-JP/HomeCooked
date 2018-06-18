from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProfileApiView, ProfilePostRudView, KitchenApiView, KitchenPostRudView
#DishViewSet,OrderViewSet



# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'groups', GroupViewSet)
# router.register(r'profiles', ProfileApiView)
# router.register(r'profiles{pk}/$', ProfilePostRudView)
# router.register(r'kitchens', KitchenApiView)
# router.register(r'kitchens{pk}/$', KitchenPostRudView)

urlpatterns = [
	url(r'^profiles/$', ProfileApiView.as_view(), name='profile-listcreate'),
    url(r'^profiles/(?P<pk>\d+)/$', ProfilePostRudView.as_view(), name='profile-rud'),
	#kitchen url
	url(r'^kitchens/$', KitchenApiView.as_view(), name='kitchen-listcreate'),
    url(r'^kitchens/(?P<pk>\d+)/$', KitchenPostRudView.as_view(), name='kitchen-rud'),

#  url(r'^', include(router.urls))
]

