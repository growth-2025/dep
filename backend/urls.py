"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.urls import path
from django.http import JsonResponse, HttpResponse


def home(request):
    return HttpResponse("Deployment successful! Django is running.")


def stock_data(request):
    data = {
        "message": "Stock data API working",
        "price": 2500,
        "volume": 100000,
        "status": "success"
    }
    return JsonResponse(data)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('stock data', stock_data),
]

