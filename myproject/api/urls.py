from django.urls import path
from .views import DomainListView

urlpatterns = [
    path("domains/", DomainListView.as_view(), name="domain-list"),
]
