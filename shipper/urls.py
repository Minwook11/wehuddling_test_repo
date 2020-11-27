from django.urls import path

from .views import ShipperView

urlpatterns = [
    path('', ShipperView.as_view()),
]
