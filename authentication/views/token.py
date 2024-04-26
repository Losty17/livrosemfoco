from django.http import HttpRequest, JsonResponse
import json

from authentication.services.get_token import GetTokenService


def get_token(request: HttpRequest):
    if not request.body:
        return JsonResponse({"error": "Body is empty"}, status=400)

    json_data = json.loads(request.body)

    success, detail, result = GetTokenService(data=json_data).perform()

    return JsonResponse({
        "success": success,
        "detail": detail,
        **result
    }, safe=False)
