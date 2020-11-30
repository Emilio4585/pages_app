from django.views.generic import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class AboutContactView(TemplateView):
    template_name = 'pages/contact.html'
