from django.urls import include, path
from rest_framework import routers
from server import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'facilities', views.FacilityViewSet)
router.register(r'scripts', views.ScriptViewSet)
router.register(r'properties', views.PropertyViewSet)
router.register(r'forms', views.FormViewSet)
router.register(r'facility_types', views.FacilityTypeViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'form_scripts', views.FormScriptViewSet)

urlpatterns = [path('', include(router.urls)), path('api/', include('rest_framework.urls', namespace='rest_framework'))]
