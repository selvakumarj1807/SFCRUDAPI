from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  StudentEnquiryViewSet

router = DefaultRouter()
router.register(r'ENQUIRY', StudentEnquiryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]