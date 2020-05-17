from django.shortcuts import render
from info.models import Graph
from info.serializers import GraphSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})

class GraphList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        graphs = Graph.objects.all()
        serializer = GraphSerializer(graphs, many=True)
        return Response(serializer.data)
