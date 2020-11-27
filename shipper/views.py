import json

from django.views import View
from django.http import JsonResponse

from .models import Shipper

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
