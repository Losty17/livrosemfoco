from django.http import JsonResponse

from core.models.profile import Profile


def get_user(request, id: int):
    if id is None:
        return JsonResponse({'error': 'No id provided'}, status=400)
    
    profile = Profile.objects.select_related("user").filter(user_id=id).first()

    if profile is None: 
        return JsonResponse({'error': 'User not found'}, status=404)
    
    user = profile.user
    
    return JsonResponse({
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'phone': user.phone,
    })
