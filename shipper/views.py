import json

from django.views import View
from django.http import JsonResponse

from .models import Shipper
from customer.models import Order

class ShipperView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            input_name = data['name']
            input_phone_number = data['phone_number']
            input_region = data['region']

            if Shipper.objects.filter(name = input_name).exists():
                return JsonResponse({'message' : 'DUPLICATE_INFORMATION'}, status = 400)
            if Shipper.objects.filter(phone_number = input_phone_number).exists():
                return JsonResponse({'message' : 'DUPLICATE_INFORMATION'}, status = 400)

            Shipper(
                name = input_name,
                phone_number = input_phone_number,
                region = input_region
            ).save()
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        return JsonResponse({'message' : 'SUCCESS'}, status = 200)

class OrderView(View):
    def get(self, request, shipper_id):
        shipper = Shipper.objects.get(id = shipper_id)
        if not(shipper):
            return JsonResponse({'message' : 'WRONG_SHIPPER_ID'}, status = 400)

        check_orders = Order.objects.filter(shipper_id = shipper_id)
        if not(check_orders):
            return JsonResponse({'mseaage' : 'NO_ORDER'}, status = 200)

        order_list = [{
            'order_id' : order.id,
            'address' : order.address,
            'quantity' : order.quantity,
        } for order in check_orders]
        return JsonResponse({'message' : order_list}, status = 200)

    def post(self, request):
        try:
            data = json.loads(request.body)
            target_order_id = data['order_id']
            target_shipper_id = data['shipper_id']

            if not(Order.objects.filter(id = target_order_id).exists()):
                return JsonResponse({'message' : 'WRONG_ORDER_ID'}, status = 400)

            if not(Shipper.objects.filter(id = target_shipper_id).exists()):
                return JsonResponse({'message' : 'WRONG_SHIPPER_ID'}, status = 400)

            if not(Order.objects.filter(id = target_order_id, shipper_id = target_shipper_id).exists()):
                return JsonResponse({'message' : 'WRONG_ORDER_SHIPPER_ID_CONNECT'}, status = 400)

            target_order = Order.objects.get(id = target_order_id)
            if target_order.status == 2:
                return JsonResponse({'message' : 'ORDER_ALREADY_FINISHED'}, status = 400)
            target_order.status = 2
            target_order.save()
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
        return JsonResponse({'message' : 'SUCCESS'}, status = 200)
