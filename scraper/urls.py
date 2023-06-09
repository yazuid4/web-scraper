from django.urls import path

from scraper import views

urlpatterns = [
   path("/", views.get_home, name='home'),
   path("/ck/<str:message>/", views.get_home, name='home-message'),
   path("/<str:message>/<str:file_id>", views.get_home, name='home-result'),
   path("/<str:file_id>", views.get_file, name='file-download')
]