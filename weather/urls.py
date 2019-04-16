from django.urls import include, path
from rest_framework import routers

from weather import views

app_name = "weather"


router = routers.DefaultRouter()
router.register(r'england', views.EnglandWeatherView, basename='weather')
router.register(r'scotland', views.ScotlandWeatherView, basename='weather')

router_2 = routers.DefaultRouter()
router_2.register(r'rainfall', views.KhGetRainFallViewset, base_name="rainfall")
router_2.register(r'tmax', views.KhGetTmaxViewset, base_name="max-temperature")
router_2.register(r'tmin', views.KhGetTminViewset, base_name="min-temperature")

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v2/', include(router_2.urls)),
    path('api/v2/add-temp/', views.KhAddTemperatureViewset.as_view()),
    path('api/v2/add-rainfall/', views.KhAddRainfallViewset.as_view())

]