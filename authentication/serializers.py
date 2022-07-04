from django.contrib.auth import password_validation
from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from authentication.models import User


class RegisterUserSerializer(ModelSerializer):
    confirm_password = CharField(
        max_length=128, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "role",
            "password",
            "confirm_password",
        ]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def validate_password(self, password):
        password_validation.validate_password(password, self.instance)
        return password

    def save(self):
        user = User(
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            email=self.validated_data["email"],
            role=self.validated_data["role"],
        )

        password = self.validated_data["password"]
        password = self.validate_password(password)
        confirm_password = self.validated_data["confirm_password"]

        if password != confirm_password:
            raise ValidationError({"password": "Passwords do not match."})

        if user.role == 1:
            user.is_staff = True

        user.set_password(password)
        user.save()

        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "role"]
