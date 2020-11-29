from django.urls import path

from .views import ShipperView, OrderView

urlpatterns = [
    path('', ShipperView.as_view()),
    path('/<int:shipper_id>', OrderView.as_view()),
    path('/check', OrderView.as_view()),
]
