from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import RegistrationSerializer
from .models import CustomerUser
from rest_framework.authtoken.models import Token

@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view(request):
	if request.method == 'POST':
		data = {}
		email = request.data.get('email', '0').lower()
		if validate_email(email) != None:
			data['error_message'] = 'That email is already in use.'
			data['response'] = 'Error'
			return Response(data)

		serializer = RegistrationSerializer(data=request.data)
		
		if serializer.is_valid():
			account = serializer.save()
			data['response'] = 'successfully registered new user.'
			data['email'] = account.email
			data['full_name'] = account.full_name
			data['pk'] = account.pk
			# token = Token.objects.get_or_create(user=account).key
			# data['token'] = token
		else:
			data = serializer.errors
		return Response(data)

def validate_email(email):
	account = None
	try:
		account = CustomerUser.objects.get(email=email)
	except CustomerUser.DoesNotExist:
		return None
	if account != None:
		return email

class ObtainAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        context = {}
        email = request.POST.get('username')
        password = request.POST.get('password')
        print(email, password)
        account = authenticate(email=email, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            context['response'] = 'Successfully authenticated.'
            context['pk'] = account.pk
            context['email'] = email.lower()
            context['token'] = token.key
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'
        return Response(context)

