from django.shortcuts import render
from django.views import View

# Create your views here.


class Inicio(View):
    def get(self, request, format=None, *args, **kwargs):
        return render(request, "index.html")

    #def post(self, request, format=None):

