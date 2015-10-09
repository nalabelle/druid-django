from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from rest_framework import reverse
from druidapi.query.models import QueryModel
from models import Result
from forms import SearchForm
import requests
import json

class IndexView(generic.View):
    """
    The view for the main page, where the search form is
    """

    def get(self, request):
        form = SearchForm
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            # Little bit of cheating, ideally the html would handle this
            # but, I felt like building the webapp in django...
            # alternatively, I could just reach over and build this.
            start = form.cleaned_data['start'].isoformat()
            end = form.cleaned_data['end'].isoformat()
            # POST the query and return the pk, so we can look it up later
            r = requests.post('http://localhost:9000/api/query/', data={'start_date': start, 'end_date': end})
            result = Result.objects.create(key=r.json()["pk"])
            result.save()
            # To the results!
            return HttpResponseRedirect("/{0}/".format(r.json()["pk"]))
        else:
            return render(request, 'index.html', {'form': form})

class ResultsView(generic.View):
    """
    When the search is executed, it needs to display the results...
    """

    def get(self, request, pk):
        result = Result.objects.get(key=pk)
        # GET the results for the key we're given
        r = requests.get("http://localhost:9000/api/query/{0}/execute/".format(pk))
        result.data = r.json()
        return render(request, 'results.html', {'result': result})

