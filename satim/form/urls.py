from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    # TransactionFormComplainsTypesViewSet,
    TransactionFormViewSet,
    # ComplaintFormTypesViewSet,
    ComplaintFormViewSet,

)

router = DefaultRouter()
# router.register(r'transaction-complain-types', TransactionFormComplainsTypesViewSet)
router.register(r'transaction-forms', TransactionFormViewSet)
# router.register(r'complaint-form-types', ComplaintFormTypesViewSet)
router.register(r'complaint-forms', ComplaintFormViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 