from django.urls import path

from .views import AboutView, AdminBodyView, BODView,MessageView, HistoryView,AdviseBodyView, ServiceView


urlpatterns = [
    path('about',AboutView.as_view(),name="about"),
    path('message',MessageView.as_view(),name="message"),
    path('history',HistoryView.as_view(),name="history"),
    path('bod',BODView.as_view(),name="bod"),
    path('adminbody',AdminBodyView.as_view(),name="adminbody"),
    path('advisorybody',AdviseBodyView.as_view(),name="advisorybody"),
    path('service',ServiceView.as_view(),name="service"),    
]
