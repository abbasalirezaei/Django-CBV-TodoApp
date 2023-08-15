from .models import Task
import django_filters
from django_filters.filters import RangeFilter

# Creating product filters
BOOLEAN_CHOICES = (
    (0, 'uncompleted'),
    (1, 'complete'),
)

class TaskFilter(django_filters.FilterSet):
    isCompleted = django_filters.TypedChoiceFilter(choices=BOOLEAN_CHOICES,label='  Sort By Status')

    class Meta:
        model = Task
        fields = ['isCompleted']
