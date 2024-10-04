from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("link/", include('link.urls'), name='link-urls'),
    path("", include("modblog.urls"), name="modblog-urls"),
]

handler404 = 'modblog.views.error_404'
