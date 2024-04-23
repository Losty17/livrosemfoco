from django.http import HttpRequest, JsonResponse
import json

from authentication.services.get_token import GetTokenService


def get_token(request: HttpRequest):
    # check if body is empty
    if not request.body:
        return JsonResponse({"error": "Body is empty"}, status=200)

    json_data = json.loads(request.body)

    success, detail, token = GetTokenService(data=json_data).perform()

    return JsonResponse({"success": success, "detail": detail, "token": token})
