from rest_framework.routers import DefaultRouter
from django.urls import path, include
from logistic.views import ProductViewSet, StockViewSet, WelcomeView


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)


# Регистрируем ViewSet для пустой страницы
# router.register('', WelcomeView, basename='welcome')
 


urlpatterns = router.urls
