from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("api/", include('api.urls')),
    path('admin/', admin.site.urls),
    path('polls/', include('models.polls.urls')),

    # test view
    # path('', views.index),
    
    path("__debug__/", include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
