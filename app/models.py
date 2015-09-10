from django.db import models

RND_DIGITS62 = 'q8YWysIz4JwSA9K6fn31GhPrTojDaZRuvXQgHVt5bkUEFce2lNMC0xdpi7mOLB'
RND_A = 69069
RND_C = 1
RND_M = 4294967296

class slink(models.Model):
    clave = models.CharField(max_length=16, primary_key=True)
    url = models.URLField(unique=True)
    fecha = models.DateTimeField(auto_now=True)
    clicks = models.PositiveIntegerField(default=0)

    def gen_clave(self):
        obj = opciones.objects.get(pk='RND_NEXT')
        n = int(obj.valor)
        obj.valor = ( (RND_A * n) + RND_C ) % RND_M
        obj.save()

        obj = opciones.objects.get(pk='RND_COUNT')
        obj.valor = int(obj.valor)+1
        obj.save()

        out = ''
        while (n != 0):
            out += RND_DIGITS62[n % 62]
            n = n // 62

        return out

    def save(self):
        self.clave = self.gen_clave()
        super(slink, self).save()

    def __str__(self):
        return 'http://64k.in/%s/' % (self.clave)


class opciones(models.Model):
    clave = models.CharField(max_length=20, primary_key=True)
    valor = models.CharField(max_length=20)

    def __str__(self):
        return '%s: %s' % (self.clave, self.valor)