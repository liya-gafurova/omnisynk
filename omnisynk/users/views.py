from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from rest_framework import status
import jwt
from django.contrib.auth import user_logged_in, authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from rest_framework_jwt.serializers import jwt_payload_handler
from omnisynk import settings
from .models import User, UserManager

DETAIL_403 = 'Can not authenticate with the given credentials or the account has been deactivated.'

@api_view(['POST'])
@permission_classes([AllowAny, ])
def authinticate(request):
    serializer = UserSigninRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    user = authenticate(username=email, password=password)
    if (user is None) or (not user.is_active):
        res = {'detail': DETAIL_403}
        return Response(res, status=status.HTTP_403_FORBIDDEN)

    payload = jwt_payload_handler(user)
    token = jwt.encode(payload, settings.SECRET_KEY)
    user_details = {}
    user_details['token'] = token
    user_logged_in.send(sender=user.__class__, request=request, user=user)

    return Response(user_details, status=status.HTTP_200_OK)

class SignInUser(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
