

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from logistic.views import  WelcomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('logistic.urls')),
    path('', WelcomeView.as_view(), name='welcome'),
    # path('products/?search=', ProductListView.as_view(), name="products_list"),
    # router.register('pruducts', ProductListView)
   ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
