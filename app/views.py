from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import DetailView, RedirectView, TemplateView

from app.models import Slink
from app.forms import slink_crear_form

from rest_framework import viewsets
from app.serializers import SlinkSerializer


class slink_crear_view(TemplateView):
    template_name = 'slink/crear.html'


class slink_ver_view(DetailView):
    model = Slink
    template_name = 'slink/ver.html'


class slink_redirect_view(RedirectView):
    permanent = False

    def get(self, request, **kwargs):
        slug = self.kwargs.get('slug', None)
        obj = get_object_or_404(Slink, slug=slug)

        if obj.estado == 'A':
            self.url = obj.url
            obj.visitas += 1
            obj.save()
            return super(slink_redirect_view, self).get(request, **kwargs)
        else:
            raise Http404


class error404(TemplateView):
    template_name = '404.html'


class error500(TemplateView):
    template_name = '500.html'



class SlinkViewSet(viewsets.ModelViewSet):
    queryset = Slink.objects.all()
    serializer_class = SlinkSerializer
