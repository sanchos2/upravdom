from django.urls import path

from datastorage import views

urlpatterns = [
    path('', views.PlacementsView.as_view(), name='index'),
]
