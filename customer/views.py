import json
import random

from django.views import View
from django.http  import JsonResponse

from .models        import Customer, Order
from product.models import Product
from shipper.models import Shipper

def address_setting(input_address):
    address_set = []
    address_set.append(''.join(input_address))
    address_set.append(''.join(input_address))
    return address_set

def order_setting(customer_id, customer_address):
    product_list = Product.objects.all()
    shipper_list = Shipper.objects.filter(region__icontains = customer_address)   
    shipper_index = 0
    random_list = random.sample(range(1, len(product_list) + 1), random.randint(1, len(product_list)))

    for random_id in random_list:
        for product in product_list:
            if product.id == random_id and product.stock > 0:
                product.stock = product.stock - 1
                product.save()
                Order(
                    customer_id = customer_id,
                    product_id  = product,
                    quantity    = 1,
                    shipper_id  = shipper_list[shipper_index],
                    address     = customer_address,
                    status      = 1
                ).save()
                shipper_index += 1
                if shipper_index > len(shipper_list) - 1:
                    shipper_index = 0
            
class JoinView(View):
    def post(self, request):
        try:
            data               = json.loads(request.body)
            input_name         = data['name']
            input_phone_number = data['phone_number']
            input_password     = data['password']
            input_address      = data['address']

            if Customer.objects.filter(phone_number = input_phone_number).exists():
                return JsonResponse({'message' : 'DUPLICATE_JOIN_INFORMATION'}, status = 400)

            address_set = address_setting(input_address)

            Customer(
                name         = input_name,
                phone_number = input_phone_number,
                password     = input_password,
                new_address  = address_set[0],
                old_address  = address_set[1]
            ).save()

            order_setting(Customer.objects.get(phone_number = input_phone_number), input_address)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        return JsonResponse({'message' : 'SUCCESS'}, status = 200)
