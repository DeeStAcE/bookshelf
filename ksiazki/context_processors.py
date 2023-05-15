from ksiazki.models import Publisher


def number_of_publishers(request):
    return {
        'pc': Publisher.objects.count()
    }
