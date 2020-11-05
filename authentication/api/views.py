from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from authentication.models import Accounts
from authentication.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
                authentication = serializer.save()
                data['response']="successfully registered new user"
                data['email'] = authentication.email
                data['username'] = authentication.username
                token= Token.objects.get(user=authentication).key
                data['token']=token
        else:
                data = serializer.errors
        return Response(data)

            