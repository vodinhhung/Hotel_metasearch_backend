from django.db.models.expressions import F
from django.http import JsonResponse
from django.core.paginator import Paginator
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from rest_framework.utils import serializer_helpers

from hotel.serializers import DomainSerializer, RootSerializer
from hotel.models import Root, Domain

def hotel_list(request, page_number = 1, page_size = 10):
    hotel_list = Root.objects.all()
    paginator = Paginator(hotel_list, page_size)
    hotels = paginator.page(page_number)

    print(hotel_list)
    print(hotels)

    # return JsonResponse(list(hotels), safe=False)
    return JsonResponse([], safe=False)

def hotel_detail(request, id):
    if request.method == "GET":
        hotel = Root.objects.get(index=id)
        print(hotel)
        serializer = RootSerializer(hotel, many=False)
        return JsonResponse(serializer.data, safe=False)

def domain_list(request):
    if request.method == "GET":
        domains = Domain.objects.all()
        serializer = DomainSerializer(domains, many=True)
        return JsonResponse(serializer.data, safe=False)