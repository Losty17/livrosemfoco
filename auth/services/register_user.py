from auth.services.get_token import GetTokenService
from core.services.service_base import ServiceBase
from django.contrib.auth.models import User


class RegisterUserService(ServiceBase):
    def __init__(self, data: dict):
        self.data = data

    def _perform(self):
        self.validate_data()
        user = self.create_user()

        success, detail, token = GetTokenService(
            should_validate_data=False, user=user
        ).perform()

        if not success:
            return False, detail, None

        user_json = {
            "id": user.id,
            "name": user.first_name,
            "email": user.email,
            "phone": user.username,
            "token": token,
        }

        return True, "User created successfully", user_json

    def validate_data(self):
        self.name = self.data.get("name")
        self.email = self.data.get("email")
        self.phone = self.data.get("phone")
        self.password = self.data.get("password")

        errors = []
        if not self.name:
            errors.append("Name is required")

        if not self.email:
            errors.append("Email is required")

        if not self.phone:
            errors.append("Phone is required")

        if not self.password:
            errors.append("Password is required")

        if errors:
            raise ValueError(errors)

    def create_user(self):
        user = User.objects.create_user(
            username=self.email,
            email=self.email,
            password=self.password,
            first_name=self.name,
        )

        return user
