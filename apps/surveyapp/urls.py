from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.display),
    url(r'^new$', views.new)]