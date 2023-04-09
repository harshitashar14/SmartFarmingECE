from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import StatusItem


class Status(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        status = StatusItem.objects.create(

                Temp = data.get('temp'),
                Humidity = data.get('humidity'),
                Moisture = data.get("moisture"),
                Is_sprinkler_on = data.get("is_sprinkler_on"),
                Crop_type =  data.get("crop_type"),
                Optimal_temp =  data.get("optimal_temp"),
                Optimal_moisture =  data.get("optimal_moisture"),
                Optimal_humidity = data.get("optimal_humidity"),
        )
        data = {
            "message": f"New item added to Cart with id: {status.id}"
        }
        return JsonResponse(data, status=201)

    def get(self, request):
        status = StatusItem.objects.all().values()
        return JsonResponse({'data':list(status), 'status':'201'})
