from django.contrib import admin
from django.urls import path, include
import cv.views
import vacancy.views
import compare.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cv/', cv.views.show_list),
    path('vacancy/', vacancy.views.show_list),
    path('compare/', compare.views.show_list),
]