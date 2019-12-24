from rest_framework import serializers

from .models import CustomerUser


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = CustomerUser
        fields = ['email', 'full_name', 'password', 'password2']
        extra_kwargs = {
				'password': {'write_only': True},
		}
    def	save(self):
        account = CustomerUser(
					email=self.validated_data['email'],
                    full_name = self.validated_data['full_name']
				)
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


class ChangePasswordSerializer(serializers.Serializer):

	old_password 				= serializers.CharField(required=True)
	new_password 				= serializers.CharField(required=True)
	confirm_new_password 		= serializers.CharField(required=True)


