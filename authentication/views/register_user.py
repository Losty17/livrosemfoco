from django.http import HttpRequest, JsonResponse
import json

from authentication.services.get_token import GetTokenService
from authentication.services.register_user import RegisterUserService


def register_user(request: HttpRequest):
    if request.method != "POST":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    json_data = json.loads(request.body)

    success, detail, user = RegisterUserService(data=json_data).perform()

    return JsonResponse({"success": success, "detail": detail, "user": user})
