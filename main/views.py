from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MainView(TemplateView):
    template_name = 'main/main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
