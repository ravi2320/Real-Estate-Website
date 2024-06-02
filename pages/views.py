from django.shortcuts import render
from django.http import HttpResponse

from listings.models import listings
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices

def index(request):
    Listing = listings.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'Listing': Listing,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
    }

    return render(request, 'pages/index.html', context)

def about(request):
    #Get all realtors
    realtors = Realtor.objects.order_by('hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)  