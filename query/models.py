from django.db import models
from django.utils import timezone
from datetime import timedelta

class QueryModel(models.Model):
    """
    This is the query model for making Druid queries.

    It will support holding all options needed for the backend, eventually.
    """

    #Timebox the queries for 1 day behind and 1 day ahead, by default
    start_date = models.DateTimeField(default=timezone.now()-timedelta(days=1))
    end_date = models.DateTimeField(default=timezone.now()+timedelta(days=1))

    #This will hold a JSON list of doubles [(string, string)]
    #for filtering the results by values
    filters = models.TextField()

