from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='root.html'), name = 'root'),
    path('main/', TemplateView.as_view(template_name='root.html'), name = 'root'),
    path('vip/', TemplateView.as_view(template_name='vip.html'), name = 'vip'),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    path('community/', include('community.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)