from . import views
from django.urls import path

app_name = 'madlibs'

urlpatterns = [
    # /food/ is the root.
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('home/result/', views.madlibs_result, name='madlibs_result'),
]
