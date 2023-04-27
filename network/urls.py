from django.urls import path
from django.views.generic import TemplateView

app_name = 'netowrk'

urlpatterns = [
path('',TemplateView.as_view(template_name="network/network.html"),name="network")
]

