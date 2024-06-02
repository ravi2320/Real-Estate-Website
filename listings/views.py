from gc import get_objects
from os import path
from django.shortcuts import get_object_or_404, render
from django.template import context
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import listings

def index(request):
    Listing = listings.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(Listing, 3)
    page = request.GET.get('page')
    paged_Listing = paginator.get_page(page)

    context = {
        'Listings': paged_Listing
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    Listing = get_object_or_404(listings, pk=listing_id)
    
    context = {
        'Listing': Listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):

    queryset_list = listings.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
