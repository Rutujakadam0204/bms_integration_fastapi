from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
    path('ok', Okk.as_view())
    # path('ok', okkk)
]
