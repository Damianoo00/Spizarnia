
from django.contrib import admin
from django.urls import path

from wyswietl.views import product_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wyswietl/', product_list_view)
]
