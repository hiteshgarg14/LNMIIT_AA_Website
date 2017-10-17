from django.conf.urls import url
from webapp import views


urlpatterns = [
    url(r'^home/', views.home_page, name="home_page"),
]
