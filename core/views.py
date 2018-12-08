from django.shortcuts import render
from django.http import HttpResponse
from .models import Planet
from random import randint
import json
from jchart import Chart
from jchart.config import Axes, DataSet, rgba
import wikipedia
from .exceptions import NotFound
# VIEWS FROM HERE :)
def index(request):
  return render(request, 'index.html')

def get_planets(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        planets = Planet.objects.filter(name__icontains = q )[:20]
        results = []
        for planet in planets:
            planet_json = {}
            planet_json['id'] = planet.id
            planet_json['label'] = planet.name
            planet_json['value'] = planet.name
            results.append(planet_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

class LineChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],
    }

    def get_datasets(self, **kwargs):
        data_scatter = [{'y': 24, 'x': '2017-01-01T21:00:00'}, {'y': 1, 'x': '2017-01-02T03:00:00'}, {'y': 7, 'x': '2017-01-02T14:00:00'}, {'y': 7, 'x': '2017-01-03T08:00:00'}, {'y': 13, 'x': '2017-01-04T00:00:00'}, {'y': 7, 'x': '2017-01-04T07:00:00'}, {'y': 19, 'x': '2017-01-05T01:00:00'}, {'y': 18, 'x': '2017-01-05T15:00:00'}, {'y': 14, 'x': '2017-01-06T00:00:00'}, {'y': 2, 'x': '2017-01-06T07:00:00'}, {'y': 18, 'x': '2017-01-07T06:00:00'}, {'y': 4, 'x': '2017-01-07T07:00:00'}, {'y': 21, 'x': '2017-01-07T21:00:00'}, {'y': 5, 'x': '2017-01-08T00:00:00'}, {'y': 16, 'x': '2017-01-08T07:00:00'}, {'y': 14, 'x': '2017-01-08T11:00:00'}, {'y': 21, 'x': '2017-01-09T04:00:00'}, {'y': 25, 'x': '2017-01-09T20:00:00'}, {'y': 9, 'x': '2017-01-10T15:00:00'}, {'y': 25, 'x': '2017-01-11T10:00:00'}, {'y': 17, 'x': '2017-01-11T17:00:00'}, {'y': 10, 'x': '2017-01-12T11:00:00'}, {'y': 7, 'x': '2017-01-12T17:00:00'}, {'y': 11, 'x': '2017-01-12T22:00:00'}, {'y': 2, 'x': '2017-01-13T04:00:00'}, {'y': 13, 'x': '2017-01-13T12:00:00'}, {'y': 12, 'x': '2017-01-14T12:00:00'}, {'y': 16, 'x': '2017-01-15T10:00:00'}, {'y': 15, 'x': '2017-01-16T00:00:00'}, {'y': 23, 'x': '2017-01-16T17:00:00'}, {'y': 15, 'x': '2017-01-17T02:00:00'}, {'y': 22, 'x': '2017-01-17T12:00:00'}, {'y': 18, 'x': '2017-01-17T15:00:00'}, {'y': 16, 'x': '2017-01-18T14:00:00'}, {'y': 7, 'x': '2017-01-19T09:00:00'}, {'y': 10, 'x': '2017-01-20T02:00:00'}, {'y': 7, 'x': '2017-01-20T13:00:00'}, {'y': 5, 'x': '2017-01-20T17:00:00'}, {'y': 15, 'x': '2017-01-20T20:00:00'}, {'y': 5, 'x': '2017-01-21T06:00:00'}, {'y': 13, 'x': '2017-01-21T18:00:00'}, {'y': 20, 'x': '2017-01-22T13:00:00'}, {'y': 20, 'x': '2017-01-22T16:00:00'}, {'y': 23, 'x': '2017-01-23T15:00:00'}, {'y': 3, 'x': '2017-01-23T20:00:00'}, {'y': 20, 'x': '2017-01-24T15:00:00'}, {'y': 19, 'x': '2017-01-24T16:00:00'}, {'y': 1, 'x': '2017-01-25T00:00:00'}, {'y': 3, 'x': '2017-01-25T02:00:00'}, {'y': 22, 'x': '2017-01-25T23:00:00'}, {'y': 6, 'x': '2017-01-26T19:00:00'}, {'y': 17, 'x': '2017-01-27T10:00:00'}, {'y': 7, 'x': '2017-01-28T09:00:00'}, {'y': 23, 'x': '2017-01-29T05:00:00'}, {'y': 19, 'x': '2017-01-29T17:00:00'}, {'y': 16, 'x': '2017-01-30T08:00:00'}, {'y': 19, 'x': '2017-01-30T09:00:00'}, {'y': 23, 'x': '2017-01-31T06:00:00'}, {'y': 18, 'x': '2017-02-01T05:00:00'}]
        data_line = [{'y': 20, 'x': '2017-01-02T00:00:00'}, {'y': 3, 'x': '2017-01-03T00:00:00'}, {'y': 2, 'x': '2017-01-04T00:00:00'}, {'y': 18, 'x': '2017-01-05T00:00:00'}, {'y': 19, 'x': '2017-01-06T00:00:00'}, {'y': 20, 'x': '2017-01-07T00:00:00'}, {'y': 5, 'x': '2017-01-08T00:00:00'}, {'y': 23, 'x': '2017-01-09T00:00:00'}, {'y': 18, 'x': '2017-01-10T00:00:00'}, {'y': 5, 'x': '2017-01-11T00:00:00'}, {'y': 6, 'x': '2017-01-12T00:00:00'}, {'y': 2, 'x': '2017-01-13T00:00:00'}, {'y': 23, 'x': '2017-01-14T00:00:00'}, {'y': 3, 'x': '2017-01-15T00:00:00'}, {'y': 24, 'x': '2017-01-16T00:00:00'}, {'y': 10, 'x': '2017-01-17T00:00:00'}, {'y': 9, 'x': '2017-01-18T00:00:00'}, {'y': 11, 'x': '2017-01-19T00:00:00'}, {'y': 10, 'x': '2017-01-20T00:00:00'}, {'y': 2, 'x': '2017-01-21T00:00:00'}, {'y': 16, 'x': '2017-01-22T00:00:00'}, {'y': 24, 'x': '2017-01-23T00:00:00'}, {'y': 3, 'x': '2017-01-24T00:00:00'}, {'y': 13, 'x': '2017-01-25T00:00:00'}, {'y': 7, 'x': '2017-01-26T00:00:00'}, {'y': 10, 'x': '2017-01-27T00:00:00'}, {'y': 7, 'x': '2017-01-28T00:00:00'}, {'y': 13, 'x': '2017-01-29T00:00:00'}, {'y': 1, 'x': '2017-01-30T00:00:00'}, {'y': 10, 'x': '2017-01-31T00:00:00'}, {'y': 7, 'x': '2017-02-01T00:00:00'}]

        return [
            DataSet(type='line',
                    label='Scatter',
                    showLine=False,
                    data=data_scatter),
            DataSet(type='line',
                    label='Line',
                    borderColor='red',
                    data=data_line)
        ]

def detail(request):
    try:
        query = request.POST['planet_search']
        planet = Planet.objects.filter(name__icontains=query)
        error = ""
        if planet is None:
            raise exceptions.NotFound
        try:
            planetdesc = wikipedia.WikipediaPage(title=query).summary
        except wikipedia.exceptions.PageError:
            planetdesc = ""
        except wikipedia.exceptions.DisambiguationError:
            planetdesc = ""
    except NotFound:
            error = "Not found " + query
    return render(request, 'detail.html', {'planet': planet, 'line_chart': LineChart(), 'planetdesc': planetdesc, 'error': error})

def add_request(request):
    if request.is_ajax():
        pass
    else: 
        return HttpResponse("error")