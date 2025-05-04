from django.contrib import admin
from django.urls import path, include
from core.views import page_not_found
from fcalmaz import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('team/', include('team.urls', namespace='team')),
    path('events/', include('events.urls', namespace='events')),
    path('users/', include('users.urls', namespace='users')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = page_not_found


admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Футбольный клуб Алмаз'