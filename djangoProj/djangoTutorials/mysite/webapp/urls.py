from django.conf.urls import url
# . means relative important, which here means the views.py within the webapp directory
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index')
]
