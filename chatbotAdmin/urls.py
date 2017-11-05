from django.conf.urls import url
from .views import api_webhook



urlpatterns = [
    url(r'^webhook/', api_webhook.as_view())
]