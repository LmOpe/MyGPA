from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
import requests

# Create your views here.

@api_view()
def activateUsersView(request, uid, token):
    """
    View to activate users email
    """
    post_url = "http://127.0.0.1:8000/auth/users/activation/"
    post_data = {'uid': uid, 'token': token}
    result = requests.post(post_url, data=post_data)
    content = result.text
    return Response(content)

@api_view(['POST'])
def resendActivationLinkView(request):
    """
    View to resend activation link to user
    """
    post_url = 'http://127.0.0.1:8000/auth/users/resend_activation/'
    email = request.POST.get('email')
    post_data = {'email': email}
    result = requests.post(post_url, data=post_data)
    content = result.text
    return Response(content)

@api_view(['PUT', "GET"])
@permission_classes([IsAuthenticated])
def passwordResetView(request, uid, token):
    """
    View to reset users password
    """
    if request.method == "PUT":
        post_url = 'http://127.0.0.1:8000/auth/users/set_password/'
        post_data = {'new_password': request.data['new_password'], 
                    're_new_password': request.data['re_new_password'], 'current_password': request.data['current_password'],
                    }
        #token = "{request.user.token}"
        print(token)
        headers = {'Authorization': "Token {}".format(token)}
        result = requests.post(post_url, data=post_data, headers=headers)
        content = result.text
        return Response(content)