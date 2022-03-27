from django.urls import path
import tours.views as tours_views

urlpatterns = [
    path('', tours_views.main_view, name='main'),
    path('departure', tours_views.departure_view, name='departure'),
    path('tour', tours_views.tour_view, name='tour')
]

handler404 = tours_views.custom_handler404
handler500 = tours_views.custom_handler500
