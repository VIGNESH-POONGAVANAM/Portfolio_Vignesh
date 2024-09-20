from django.urls import path
from .views import portfolio_view,storedb

urlpatterns = [
    path('',portfolio_view,name='portfolio'),
    path('store/',storedb,name="storedb"),
]
