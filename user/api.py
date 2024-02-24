from django.http import JsonResponse
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from .form import SignupForm
from django.contrib.auth.forms import PasswordChangeForm


@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = "success"

    form = SignupForm(
        {
            "username": data.get("username"),
            "email": data.get("email"),
            "prefix": data.get("prefix"),
            "firstName": data.get("firstName"),
            "lastName": data.get("lastName"),
            "role": data.get("role"),
            "password1": data.get("password1"),
            "password2": data.get("password2"),
        }
    )

    if form.is_valid():
        form.save() #save ลง database

    else:
        print(form.errors)
        message = "error"
    return JsonResponse({"message": message})

@api_view(["GET"])
def me(request):
    return JsonResponse(
        {
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "firstName": request.user.firstName,
            "lastName": request.user.lastName,
            "role": request.user.role
        }
    )


    
# change Password
# @api_view(["POST"])
# def changePassword(request):
#     user = request.user

#     form = PasswordChangeForm(data=request.POST, user=user)

#     if form.is_valid():
#         form.save()

#         return JsonResponse({"message": "success"})
#     else:
#         return JsonResponse({"message": form.errors.as_json()}, safe=False)
