# from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
# from django.views import View


def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request):
    return render(request, 'tours/departure/departure.html')


def tour_view(request):
    return render(request, 'tours/tour/tour.html')


def custom_handler404(request, exception):
    # Call when Http404 raised
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    # Call when raised some python exception
    return HttpResponseServerError('Ошибка сервера!')
