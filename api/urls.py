from django.urls import path, include
from .views import ApiIndexView

urlpatterns = [
    path('', ApiIndexView, name='index' )
]
