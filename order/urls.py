from django.urls import path
from . import views

urlpatterns = [
    path('event/',views.EventList.as_view(),name='event'),
    path('create/event/',views.CreateEvent.as_view(),name='create_event'),
    path('event/<int:id>',views.EventDetailView.as_view(),name='sigle_event'),
]