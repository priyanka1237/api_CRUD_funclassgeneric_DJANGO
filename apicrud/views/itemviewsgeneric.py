'''
Created on 28-Jun-2019

@author: netset
'''

from rest_framework import generics
from apicrud.models import Item
from apicrud.serializers import ItemSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer