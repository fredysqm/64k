from django.db import models
from django.conf import settings



ESTADO_SLINK = (
    ('A', 'Activo'),
    ('D', 'Deshabilitado'),
)


RND_A = getattr(settings, 'SLINK_RND_A')
RND_C = getattr(settings, 'SLINK_RND_C')
RND_M = getattr(settings, 'SLINK_RND_M')
RND_DIGITS62 = getattr(settings, 'SLINK_RND_DIGITS62')
SLINK_URL = getattr(settings, 'SLINK_URL')


def gen_slug():
    obj = Opcion.objects.get(pk='RND_NEXT')
    n = int(obj.valor)
    obj.valor = ( (RND_A * n) + RND_C ) % RND_M
    obj.save()

    obj = Opcion.objects.get(pk='RND_COUNT')
    obj.valor = int(obj.valor)+1
    obj.save()

    out = ''
    while (n != 0):
        out += RND_DIGITS62[n % 62]
        n = n // 62
    return out


class Slink(models.Model):
    slug = models.CharField(max_length=16, unique=True)
    url = models.URLField(verbose_name='URL Largo')
    visitas = models.PositiveIntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)
    acceso = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=1, default='A', choices=ESTADO_SLINK)

    def save(self, *args, **kwargs):
        if getattr(self, '_image_changed', True):
            small=rescale_image(self.image,width=100,height=100)
            self.image_small=SimpleUploadedFile(name,small_pic)
        super(Slink, self).save(*args, **kwargs)

    def __str__(self):
        return SLINK_URL + ('%s/' % (self.slug))


class Opcion(models.Model):
    clave = models.CharField(primary_key=True, max_length=20)
    valor = models.CharField(max_length=20)

    def __str__(self):
        return '%s: %s' % (self.clave, self.valor)

    class Meta:
        verbose_name_plural = 'opciones'