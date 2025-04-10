from django.db import models

class Kategorija(models.Model):
    pavadinimas = models.CharField(max_length=100)

    def __str__(self):
        return self.pavadinimas

class Knyga(models.Model):
    pavadinimas = models.CharField(max_length=200)
    aprasymas = models.TextField()
    kaina = models.DecimalField(max_digits=6, decimal_places=2)
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE, related_name='kat_knyga')

    def __str__(self):
        return self.pavadinimas


# python manage.py shell

# from katalogas.models import Kategorija, Knyga
#
# k1 = Kategorija.objects.create(pavadinimas='Romanas')
# k2 = Kategorija.objects.create(pavadinimas='Mokslinė')
# k3 = Kategorija.objects.create(pavadinimas='Medicina')
#
# Knyga.objects.create(pavadinimas='Knyga A', aprasymas='Aprašymas A', kaina=10.99, kategorija=k1)
# exit()




