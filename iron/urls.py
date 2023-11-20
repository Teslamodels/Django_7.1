from django.urls import path
from .views import Iron, Man, Real

urlpatterns = [
    path('', Iron.as_view(), name='Iron'),
    path('iron/', Man.as_view(), name='Man'),
    path('motiv/', Real.as_view(), name="Real"),
]