from django.shortcuts import render

from .models import Produkt

# Create your views here.

#CRUD

def product_list_view(request):
    produkt_object = Produkt.objects.all()
    context = {
        'produkty' : produkt_object
    }
    return render(request, "wyswietl/index.html", context)