from django.urls import path

from .views import HomePageView, AboutPageView, AboutContactView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', AboutContactView.as_view(), name='contact')
]
