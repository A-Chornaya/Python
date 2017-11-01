from rest_framework import renderers
from rest_framework.response import Response
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import generics
from sushi_rinjin.models.ingredients import Ingredients
from sushi_rinjin.models.ingredients import IngredSerializer


def ingred_rest(request):
    return render(request, 'sushi_rinjin/for_rest/ingred_rest.html')


class IngredList(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredSerializer


class IngredDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    serializer_class = IngredSerializer
