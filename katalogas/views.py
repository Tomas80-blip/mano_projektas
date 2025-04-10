from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Knyga, Kategorija
from .forms import KnygaForm
from django.db.models import Count, Avg, Max, Min, Q


def pagrindinis(request):
    q = request.GET.get('q')
    if q:
        knygos = Knyga.objects.filter(Q(pavadinimas__icontains=q) | Q(kategorija__pavadinimas__icontains=q))
    else:
        knygos = Knyga.objects.all()
    return render(request, 'pagrindinis.html', {'knygos': knygos})


def prideti_knyga(request):
    if request.method == 'POST':
        form = KnygaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagrindinis')
    else:
        form = KnygaForm()
    return render(request, 'knyga_form.html', {'form': form})


class RedaguotiKnyga(UpdateView):
    model = Knyga
    form_class = KnygaForm
    template_name = 'knyga_form.html'
    success_url = reverse_lazy('pagrindinis')


class TrintiKnyga(DeleteView):
    model = Knyga
    template_name = 'trinti_knyga.html'
    success_url = reverse_lazy('pagrindinis')


def statistika(request):
    kategorijos = Kategorija.objects.annotate(
        knygu_kiekis=Count('kat_knyga'),
        vid_kaina=Avg('kat_knyga__kaina'),
        max_kaina=Max('kat_knyga__kaina'),
        min_kaina=Min('kat_knyga__kaina')
    )
    brangiausia = Knyga.objects.order_by('-kaina').first()
    pigiausia = Knyga.objects.order_by('kaina').first()
    return render(request, 'statistika.html', {
        'kategorijos': kategorijos,
        'brangiausia': brangiausia,
        'pigiausia': pigiausia
    })

