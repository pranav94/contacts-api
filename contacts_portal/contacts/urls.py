from django.conf.urls import url
from rest_framework import routers
from .views import ContactViewSet


app_name = 'Contacts'

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = router.urls