from django import forms
from datetimewidget.widgets import DateTimeWidget

class SearchForm(forms.Form):
    """
    This holds the information included in the search form, for POSTing to the backend
    """

    start = forms.DateTimeField(label='Start Date',widget=DateTimeWidget(usel10n=True))
    end = forms.DateTimeField(label='End Date',widget=DateTimeWidget(usel10n=True))

