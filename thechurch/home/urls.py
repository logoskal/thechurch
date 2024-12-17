from django.urls import path, include
import home.views as views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home-page'),
    path('welcome/', views.home, name='welcome-page'),
    path('about/', views.about, name='welcome-page'),
    path('socials/', views.socials_button, name='socials-button-page'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
