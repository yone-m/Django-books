from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import ContactForm

# Create your views here.

class Top(generic.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')
    template_name = 'contact/top.html'
    
class Thanks(generic.TemplateView):
    template_name = 'contact/thanks.html'