import json

from django.views import View
from django.http import JsonResponse

from .models import Customer, Order
from product.models import Product

def address_setting(input_address):
    address_set = []
    address_set.append('new ' + ''.join(input_address))
    address_set.append('old ' + ''.join(input_address))
    return address_set

class JoinView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            input_name = data['name']
            input_phone_number = data['phone_number']
            input_password = data['password']
            input_address = ['address']

            if Customer.objects.filter(phone_number = input_phone_number).exists():
                return JsonResponse({'message' : 'DUPLICATE_JOIN_INFORMATION'}, status = 400)

            address_set = address_setting(input_address)

            Customer(
                name = input_name,
                phone_number = input_phone_number,
                password = input_password,
                new_address = address_set[0],
                old_address = address_set[1]
            ).save()
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        return JsonResponse({'message' : 'SUCCESS'}, status = 200)
