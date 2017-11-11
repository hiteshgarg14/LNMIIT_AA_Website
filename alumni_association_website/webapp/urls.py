from django.conf.urls import url
from webapp import views


urlpatterns = [
    url(r'^$', views.home_page, name="webapp_home_page"),
    url(r'^logout/$', views.logout, name="webapp_logout"),
]
