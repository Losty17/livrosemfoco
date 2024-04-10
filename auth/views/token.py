from django.http import HttpRequest, JsonResponse
import json

from auth.services.get_token import GetTokenService


def get_token(request: HttpRequest):
    json_data = json.loads(request.body)

    GetTokenService(
        data=json_data
    )
    
    

    