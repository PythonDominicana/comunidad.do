from django.urls import path

from . import views


app_name = "events"

urlpatterns = (
    # urls for Event
    path('',
         views.EventListView.as_view(),
         name='event_list'),
    path('create/',
         views.EventCreateView.as_view(),
         name='event_create'),
    path('<slug:slug>/',
         views.EventDetailView.as_view(),
         name='event_detail'),
    path('update/<slug:slug>/',
         views.EventUpdateView.as_view(),
         name='event_update'),
)
