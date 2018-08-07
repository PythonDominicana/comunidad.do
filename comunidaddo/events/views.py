from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Event
from .forms import EventForm


class EventListView(ListView):
    model = Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.pk
        return initial


class EventDetailView(DetailView):
    model = Event


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
