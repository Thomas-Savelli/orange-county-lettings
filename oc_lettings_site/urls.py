from django.contrib import admin
from django.urls import path, include

from . import views


handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('404/', views.custom_404, name='custom_404'),
    path('500/', views.custom_500, name='custom_500')
]
