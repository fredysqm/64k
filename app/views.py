from django.shortcuts import render

from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView

from app.models import slink
from app.forms import slink_crear_form


class slink_crear_view(CreateView):
    form_class = slink_crear_form
    template_name = 'slink/crear.html'
    def get_success_url(self):
        return reverse('slink_ver_url', args=(self.object.clave,))

class slink_ver_view(DetailView):
    model = slink
    template_name = 'slink/ver.html'

class slink_redirect_view(DetailView):
    model = slink
    template_name = 'slink/redirect.html'