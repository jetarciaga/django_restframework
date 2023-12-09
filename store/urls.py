from django.urls import path, include

from rest_framework.routers import DefaultRouter

from store import views


router = DefaultRouter()
router.register('products', views.ProductViewSet)

app_name = 'store'

urlpatterns = [
    path('', include(router.urls))
]