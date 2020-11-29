import json

from django.views import View
from django.http  import JsonResponse

from .models import Product, Provider

class ProviderView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            Provider(
                name            = data['name'],
                business_number = data['business_number'],
                phone_number    = data['phone_number']
            ).save()
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        return JsonResponse({'message' : 'SUCCESS'}, status = 200)

    def delete(self, request, *args, **kwargs):
        target_business_number = request.GET.get('business_number', None)

        if Provider.objects.filter(business_number = target_business_number):
            target_provider = Provider.objects.get(business_number = target_business_number)
            target_provider.delete()

            return JsonResponse({'message' : 'SUCCESSFULLY_DELETE'}, status = 200)
        return JsonResponse({'message' : 'WRONG_BUSINESS_NUMBER'}, status = 400)

class ProductView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            input_name     = data['name']
            input_provider = data['provider']
            input_price    = data['price']
            input_stock    = data['stock']

            if not(Provider.objects.filter(name = input_provider).exists()):
                return JsonResponse({'message' : 'WRONG_PROVIDER'}, status = 400)

            if Product.objects.filter(name = input_name).exists():
                return JsonResponse({'message' : 'DUBPLICATE_PRODUCT_NAME'}, status = 400)

            Product(
                name        = input_name,
                provider_id = Provider.objects.get(name = input_provider),
                price       = input_price,
                stock       = input_stock
            ).save()
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)

        return JsonResponse({'message': 'SUCCESS'}, status = 200)
