from django.shortcuts import render

from django.views.generic import TemplateView

from .other import my_weather

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'base-index.html'

    def get_context_data(self, **kwargs):
        current_weather = my_weather()

        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({'weather': current_weather})
        return context