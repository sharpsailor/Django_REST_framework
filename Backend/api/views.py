from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view([ "GET"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "content", "price"])
    return Response(data)


# Api_view to Django View
# @api_view([ "POST"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API VIEW
#     """
    
#     # Hard Coding
#     # if request.method != "GET":
#     #     return Response({"details":" GET not allowed why dont you understand "},status=405)
    
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=["id", "title", "content", "price"])
#         return JsonResponse(data)
    
    
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=["id", "title", "content", "price"])
#         return JsonResponse(data)
    #     print(data)
    #     # SerialIZE the Dictonary to JSON
    # json_data = json.dumps(data)
    # # return JsonResponse(data)
    # return HttpResponse(json_data,headers={'Content-Type':"application/json"})
    # return HttpResponse(data)


# def api_home(request,*args,**kwargs):
#     model_data=Product.objects.all().order_by("?").first()
#     data ={}
#     if model_data:
#         data['id'] = model_data.id
#         data['title'] = model_data.title
#         data['content'] = model_data.content
#         data['price'] = model_data.price

#         # Serialization
#         # take representations here Model instance (model Data) , turn a Python dictionary to a JSON to  my Clients
#     return JsonResponse(data)


# Manually ECHOING GET DATA FROM CLIENT
# def api_home (request,*args ,**kwargs):
#     # request.body
#     print(request.GET)
#     print(request.POST)
#     body = request.body
#     data ={}
#     try:
#         data = json.loads(body) # string of JSON data a-> Python dictonary
#     except:
#         pass
#     print(data)
#     # data['headers'] = request.headers # reque0st.META-> gives request.headers was used in old
#     # print(request.headers)
#     # json.dumps(dict(request.headers))
#     data['params'] = dict(request.GET)
#     data['headers'] =dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)
