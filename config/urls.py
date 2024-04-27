from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('', include('apps.core.api.v1.urls'), name='core',),
        path('', include('apps.plants.api.v1.urls'), name='plants'),
        path('', include('apps.authentication.api.v1.urls'), name='authentication'),
    ])),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)  # new