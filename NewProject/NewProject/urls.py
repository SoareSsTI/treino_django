from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('membros/', include('membros.urls')),
    path('admin/', admin.site.urls),
]
