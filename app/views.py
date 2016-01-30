from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, RedirectView, TemplateView

from app.models import slink
from app.forms import slink_crear_form



class slink_crear_view(CreateView):
    form_class = slink_crear_form
    template_name = 'slink/crear.html'

    def get_success_url(self):
        return reverse('slink_ver_url', args=(self.object.slug,))


class slink_ver_view(DetailView):
    model = slink
    template_name = 'slink/ver.html'


class slink_redirect_view(RedirectView):
    permanent = False

    def get(self, request, **kwargs):
        slug = self.kwargs.get('slug', None)
        obj = get_object_or_404(slink, slug=slug)
        
        if obj.estado == 'A' or obj.estado =='I':
            self.url = obj.url
            obj.visitas += 1
            obj.estado = 'A'
            obj.save()
            return super(slink_redirect_view, self).get(request, **kwargs)
        else:
            raise Http404


class error404(TemplateView):
    template_name = '404.html'


class error500(TemplateView):
    template_name = '500.html'