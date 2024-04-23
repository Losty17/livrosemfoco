from authentication.models.sessions import Session
from core.services.service_base import ServiceBase
from uuid import uuid4
from django.contrib.auth.models import User


class GetTokenService(ServiceBase):
    def __init__(
        self, data: dict = None, should_validate_data: bool = True, user: User = None
    ):
        self.data = data
        self.should_validate_data = should_validate_data
        self.user = user

    def _perform(self):
        if self.should_validate_data:
            self.validate_data()

        token = self.get_token()

        return True, "Token generated successfully", token

    def validate_data(self):
        self.email = self.data.get("email", None)
        self.password = self.data.get("password", None)

        errors = []
        if not self.email:
            errors.append("Email is required")

        if not self.password:
            errors.append("Password is required")

        if errors:
            return False, ", ".join(errors), None

    def get_token(self):
        if not self.user:
            self.user = User.objects.filter(username=self.email).first()

        # authenticate user with provided password

        if self.should_validate_data:
            if not self.user.check_password(self.password):
                raise ValueError("Invalid password")

        # generate token
        token = str(uuid4())

        Session.objects.create(user=self.user, session_key=token)

        return token
