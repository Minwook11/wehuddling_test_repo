from django.urls import path

from .views import ProviderView, ProductView

urlpatterns = [
    path('/provider', ProviderView.as_view()),
    path('', ProductView.as_view()),
]
