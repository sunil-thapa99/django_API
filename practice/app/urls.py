from django.urls import path
from .views import(
	registration_view,
    ObtainAuthTokenView
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'app'

urlpatterns = [
	# path('check_if_account_exists/', does_account_exist_view, name="check_if_account_exists"),
	# path('change_password/', ChangePasswordView.as_view(), name="change_password"),
	# path('properties', account_properties_view, name="properties"),
	# path('properties/update', update_account_view, name="update"),
 	path('login', ObtainAuthTokenView.as_view(), name="login"), 
	path('register', registration_view, name="register"),

]
