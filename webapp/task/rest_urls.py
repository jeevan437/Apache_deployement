from django.conf.urls import url,include
from .viewsets import EmpViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('emp_details', EmpViewSet)

urlpatterns = [
    # url(r'store_api/', StoreViewAPI.as_view()),
    # url(r'store_ret/(?P<pk>\d+)/', StoreRetrieveAPI.as_view()),
    url(r'',include(router.urls))
]

urlpatterns += router.urls