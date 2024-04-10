from django.http import HttpRequest, JsonResponse
import json

from authentication.services.get_token import GetTokenService


def get_token(request: HttpRequest):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    json_data = json.loads(request.body)

    success, detail, token = GetTokenService(data=json_data)

    return JsonResponse({"success": success, "detail": detail, "token": token})
