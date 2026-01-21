from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse

def get_nepse_live(request):
    try:
        url = "https://nepalipaisa.com/api/GetStockLive?"
        response = requests.get(url, timeout=10)

        # Convert to JSON
        data = response.json()

        return JsonResponse({
            "status": "success",
            "source": "Nepali Paisa",
            "data": data
        })

    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)
