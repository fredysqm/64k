from django.db import models

RND_DIGITS62 = 'q8YWysIz4JwSA9K6fn31GhPrTojDaZRuvXQgHVt5bkUEFce2lNMC0xdpi7mOLB'
RND_A = 69069
RND_C = 1
RND_M = 4294967296

class slink(models.Model):
    keyword = models.CharField(max_length=16, primary_key=True)
    url = models.URLField()
    fecha = models.DateTimeField(auto_now=True)
    clicks = models.PositiveIntegerField(default=0)

    def gen_keyword(self):
        obj1 = options.objects.get(pk='RND_NEXT')
        n = int(obj1.value)
        obj1.value = ( (RND_A * n) + RND_C ) % RND_M
        obj1.save()
        obj2 = options.objects.get(pk='RND_COUNT')
        obj2.value = int(obj2.value)+11
        obj2.save

        out = ''
        while (n != 0):
            out += RND_DIGITS62[n % 62]
            n = n // 62

        return out

    def save(self):
        self.keyword = self.gen_keyword()
        super(slink, self).save()

    def __str__(self):
        return '%s' % (self.keyword)


class options(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    value = models.CharField(max_length=20)