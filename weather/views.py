import datetime
import json
import os

from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView

from weather import models
from weather import serializers
from weather.utils import prepare_tmax_dataset, prepare_rainfall_dataset, prepare_tmin_dataset

DATA_DIR = os.path.dirname(__file__) + '/../data'


def prep_query(self):
    country = self.request.query_params.get("country", "England")
    start_year = self.request.query_params.get("sy")
    end_year = self.request.query_params.get("ey")
    start_month = self.request.query_params.get("sm")
    end_month = self.request.query_params.get("em")
    s_date_str = "{0}{1}{2}".format(start_year, start_month, "01")
    e_date_str = "{0}{1}{2}".format(end_year, end_month, "01")
    start_date = datetime.datetime.strptime(s_date_str, '%Y%d%m').date()
    end_date = datetime.datetime.strptime(e_date_str, '%Y%d%m').date()
    print(start_date, end_date, "hld")
    if start_year and start_month and end_month and end_year:
        return self.queryset.filter(date__gte=start_date,
                                    date__lte=end_date,
                                    country=country)
    else:
        return self.queryset.filter(country=country)


class EnglandWeatherView(viewsets.ViewSet):

    def list(self, request):
        metric = request.GET['metric']
        with open(os.path.join(DATA_DIR, metric, 'england/data.json')) as f:
            data = json.loads(f.read())
        return Response(data)


class ScotlandWeatherView(viewsets.ViewSet):

    def list(self, request):
        metric = request.GET['metric']
        with open(os.path.join(DATA_DIR, metric, 'scotland/data.json')) as f:
            data = json.loads(f.read())
        return Response(data)


class KhGetRainFallViewset(viewsets.ReadOnlyModelViewSet):
    """
        - Returns all rainfall data by country (country) and date (year & month)
        - If no date is specified it returns all rainfall data for the specified country
        - Default country is "england"
    """
    queryset = models.KhRainFall.objects.all()
    serializer_class = serializers.KhRainFallSerializer

    def get_queryset(self):
        return prep_query(self)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        data = json.loads(json.dumps(serializer.data))
        dataset = prepare_rainfall_dataset(data, self.request.query_params.get("country", "England"))
        return Response(dataset)


class KhAddRainfallViewset(APIView):
    serializer_class = serializers.KhAddRainfallSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("New record was updated successfully")


class KhGetTmaxViewset(viewsets.ReadOnlyModelViewSet):
    """
        - Returns all temperature data by country (country) and date (year & month)
        - If no date is specified it returns all temperature data for the specified country
        - Default country is "england"
    """
    queryset = models.KhTmax.objects.all()
    serializer_class = serializers.KhTemperatureSerializer

    def get_queryset(self):
       return prep_query(self)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        data = json.loads(json.dumps(serializer.data))
        dataset = prepare_tmax_dataset(data, self.request.query_params.get("country", "England"))
        return Response(dataset)


class KhGetTminViewset(viewsets.ReadOnlyModelViewSet):
    """
        - Returns all temperature data by country (country) and date (year & month)
        - If no date is specified it returns all temperature data for the specified country
        - Default country is "england"
    """
    queryset = models.KhTmin.objects.all()
    serializer_class = serializers.KhMinTemperatureSerializer

    def get_queryset(self):
       return prep_query(self)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        data = json.loads(json.dumps(serializer.data))
        dataset = prepare_tmin_dataset(data, self.request.query_params.get("country", "England"))
        return Response(dataset)


class KhAddTemperatureViewset(APIView):
    serializer_class = serializers.KhAddTemperatureSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("New record was updated successfully")


