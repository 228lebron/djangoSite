from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Quote
from .scraper import scrape_price


# Create your views here.
def index(request):
    quotes = Quote.objects.all()
    current_user_groups = request.user.groups.values_list("name", flat=True)
    context = {
        'quotes': quotes,
        "is_sale": "Sale" in current_user_groups,
        "is_product_man": "Product" in current_user_groups,
    }
    return render(request, 'home.html', context)

def update(request):
    quotes = Quote.objects.all()
    for quote in quotes:
        quote.compel_price = scrape_price(quote.part_number, quote.brand)
        quote.save()
    #return render(request, 'home.html', {'quotes': quotes})
    #return redirect('home')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_quote(request):
    pass




