from django.http import HttpResponse


def custom_404_view(request, exception=None):
    return HttpResponse(request, 'store/error404.html', status=404)
