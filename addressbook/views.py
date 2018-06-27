# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from models import AddressBook
from django.http import JsonResponse
from django.shortcuts import render
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
import rest_framework_filters as filters


# Create your views here.
def index(request):
    return render(request, 'index.html', {"addresses": AddressBook.objects.all()})
    #return HttpResponse("Hello, world from addressbook. %s" %str(AddressBook.objects.all()))

"""def api(request):

    addresses = AddressBook.objects.all()
    out = []
    
    for a in addresses:
        out.append({"first_name": a.first_name, "last_name": a.last_name, "phone": a.phone})
    
    return JsonResponse({"data": out})"""

# Serializers define the API representation.    
class AddressBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddressBook
        fields = ('id', 'first_name','last_name','phone','address','city','state','country','zipcode', 'email')


class AddressBookFilter(filters.FilterSet):
    first_name = filters.AllLookupsFilter(name="first_name")

    class Meta:
        model = AddressBook
        fields = ['first_name']

# ViewSets define the view behavior.
class AddressBookViewSet(viewsets.ModelViewSet):
    queryset = AddressBook.objects.all()
    serializer_class = AddressBookSerializer
    filter_class = AddressBookFilter

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'addresses', AddressBookViewSet)

def new(request):

    a = AddressBook(first_name = request.POST['first_name'], 
                last_name = request.POST['last_name'], 
                phone = request.POST['phone'],
                address = request.POST['address'],
                city = request.POST['city'],
                state = request.POST['state'],
                country = request.POST['country'],
                zipcode = request.POST['zipcode'],
                email = request.POST['email'])

    a.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def edit(request):
    a = AddressBook.objects.get(id=request.POST['id']) 
    a.first_name=request.POST['first_name']
    a.last_name=request.POST['last_name']
    a.phone=request.POST['phone']
    a.address=request.POST['address']
    a.city=request.POST['city']
    a.state = request.POST['state']
    a.country = request.POST['country']
    a.zipcode = request.POST['zipcode']
    a.email = request.POST['email']
    a.create_date = request.POST['create_date']
    a.modified_date = request.POST['modiefied_date']
    a.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def delete(request):
    if request.POST['submit'] == 'delete':
        a = AddressBook.objects.get(id=request.POST['id'])
        a.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    
