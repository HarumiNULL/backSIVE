import django_filters
from api.models import Schedule

class ScheduleFilter(django_filters.FilterSet):
  class Meta:
    model = Schedule
    fields = ['optical']
