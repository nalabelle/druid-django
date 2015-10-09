from django.db import models

class Result(models.Model):
    """
    This is a model for returning a search from the DruidAPI
    """

    #this holds the PK from the query API
    key = models.IntegerField(blank=True)

    #this holds the data returned when the page is accessed
    data = models.TextField(blank=True)
