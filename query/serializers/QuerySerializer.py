from rest_framework import serializers
from druidapi.query.models import QueryModel

class QuerySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    start_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField(required=False)
    filters = serializers.CharField(required=False)

    def create(self, validated_data):
        return QueryModel.objects.create(**validated_data)

