from pydruid.client import *
import pandas as pd

class DruidConnection:
    """
    This class facilitates the backend connection with the Druid Datastore

    Currently it's pretty simple and only returns top queries for a specified
    timeframe, but it's going to be built out to be a full interface supporting
    the full Druid query language, available here:
    http://druid.io/docs/0.8.1/querying/querying.html
    """

    ## The default query connection
    query = PyDruid('http://localhost:8084/', 'druid/v2')

    def build(self, interval='2012-10-01/p10y'):
        top = self.query.topn(
                #currently, I only have a wikipedia set I'm ingesting
                #this would be the easiest place to segment for security
                datasource='wikipedia',
                granularity='all',
                intervals=interval,
                aggregations={'edit_count': longsum('count')},
                dimension='page',
                metric='edit_count',
                threshold=10
                )

        # return a pandas dataframe, empty or not
        df = self.query.export_pandas()
        if df is None:
            df = pd.DataFrame()
        return df

