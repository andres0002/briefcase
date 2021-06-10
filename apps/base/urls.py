from django.urls import path
from apps.base.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]