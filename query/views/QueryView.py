from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import viewsets
from druidapi.query.models import QueryModel
from druidapi.query.serializers.QuerySerializer import QuerySerializer
from druidapi.backend.DruidConnection import DruidConnection
from rest_pandas.renderers import PandasJSONRenderer

class QueryViewSet(viewsets.ModelViewSet):
    model = QueryModel
    serializer_class = QuerySerializer
    queryset = QueryModel.objects.all()

    def create(self, request):
        """
        Creates a search object for Druid
        """
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns information about a Druid Query
        """
        result = self.get_object()
        serializer = self.get_serializer(result)
        return Response(serializer.data)

    @detail_route(['get',], renderer_classes=[PandasJSONRenderer,])
    def execute(self, request, *args, **kwargs):
        """
        Submits the query and returns the result
        """
        query = self.get_object()
        dc = DruidConnection()
        """
        Instead of building the interval here, as more options are supported,
        it would make more sense to pass over the particular object we'd like
        to execute, and pull out what we need from it.
        """
        result = dc.build(interval="{0}/{1}".format(query.start_date.isoformat(), query.end_date.isoformat()))
        return Response(result)

