from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', views.index,name='index'),
    path('', views.home,name='home'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
