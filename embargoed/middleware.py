import maxminddb
from django.shortcuts import render


# Using an Open-Source IP db released under an Apache2 license: https://github.com/geoacumen/geoacumen-country
reader = maxminddb.open_database('embargoed/Geoacumen-Country.mmdb')

def embargo(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    ip = ""
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    data = reader.get(ip)
        
    if data:
        country = data['country']['iso_code']
        print(country)
        if country == 'RU':
            return True
        else:
            return False

class EmbargoedMiddlewareTemplate:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        embargoed = embargo(request)
        if embargoed:
            return render(request, 'embargoed/index.html')
        else:
            response = self.get_response(request)
            return response
            
