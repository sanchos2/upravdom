from django.views.generic import ListView

from datastorage.models import Placement


class PlacementsView(ListView):
    """Вывод данных в шаблон."""

    model = Placement
    template_name = 'index.html'
    context_object_name = 'placements'
