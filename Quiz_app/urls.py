from django.contrib import admin
from django.urls import path
from Quiz_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.data_fill,name='playgame'),
    path('scroe/',views.count_data,name='score'),
]