from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    print(result)
    content = result.text
    return Response(content)