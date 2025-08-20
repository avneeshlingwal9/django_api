from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):

    #return JsonResponse({"message": "Hello World"}) ## Raw hardcoded data, but we may want to use, data from database itself
    body = json.loads(request.body) 

    
    data = {}

    try: 
        data = body
    except:

        pass

    data['params'] = dict(request.GET) # url query parameters.  
    data['headers'] = dict(request.headers) 
    data['content-type'] = request.content_type



    return JsonResponse(data)
