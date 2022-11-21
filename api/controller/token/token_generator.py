import uuid
from datetime import datetime, timezone, timedelta
from api.controller.token.token_base_class import TokenBaseClass
from api.library.jwt_wrapper import JWTWrapper
from api.models import AuthToken, Administrator
from api.exceptions.token_exceptions import TokenGeneratorError


class AdministratorToken (TokenBaseClass) :

    def __init__(self):
        self.jwt = JWTWrapper()


    def generate_access_token(self, administrator):
        try:
            payload = {
                "user_id": administrator.id,
                "user_name": administrator.username,
                "first_name": administrator.first_name,
                "last_name": administrator.last_name,
                "email": administrator.email,
                "user_type": "ADMINISTRATOR",
                "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=15)
            }
            return self._jwt.generate_access_token(payload)
        except Exception as e:
            raise e

    def generate_refresh_token(self, key):
        try:
            return self._jwt.generate_refresh_token(key)
        except Exception as e:
            raise e

    def create_tokens(self, administrator):
        try:
            administrator = Administrator.objects.get(email=administrator.email, is_active=True)
            user_tokens = self.generate_tokens(administrator)
            token_instance = AuthToken.objects.create(
                administrator=administrator,
                access_token=user_tokens["access"],
                refresh_token=user_tokens["refresh"],
                is_revoked=False,
                generated_at=datetime.now(tz=timezone.utc)
            )
            token_instance.save()
            return token_instance
        except Administrator.DoesNotExist:
            raise TokenGeneratorError(
                "User not found"
            )
        except Exception as e:
            raise e
    
    def generate_tokens(self, administrator):
        try:
            access_token = self.generate_access_token(administrator)
            refresh_token = self.generate_refresh_token(str(uuid.uuid4()))
            if access_token and refresh_token != None:
                return {
                    "access": access_token,
                    "refresh": refresh_token
                }
            raise TokenGeneratorError(
                "Failed to generate tokens"
            )
        except TokenGeneratorError as tge:
            raise tge
        except Exception as e:
            raise e

