import os
import jwt


class JWTWrapper:

    def __init__(self):

        try:
            self._audience = os.environ.get(
                "JWT_AUDIENCE")
            self._issuer = os.environ.get("JWT_ISSUER")
            self._algorithm = os.environ.get("JWT_ALGORITHM") or "RS256"

            with open(os.environ.get("../keys/private.pem"), 'rb') as f:
                self._private_key = f.read()
            self._primary_payload_data = {
                "iss": self._issuer,
                "aud": self._audience,
            }
            with open(os.environ.get("keys/public.pem"), "rb") as f:
                self._public_key = f.read()
        except FileNotFoundError as file_error:
            raise Exception(f"Key files are not available. {file_error}")
        except Exception as error:
            raise Exception(f"Error while initializing JWTWrapper. {error}")

    def generate_refresh_token(self, refresh_token_key: str) -> str:
        try:
            payload = {}
            payload['refresh_token_key'] = refresh_token_key
            payload['iss'] = self._issuer
            payload['aud'] = self._audience
            return jwt.encode(payload, self._private_key, algorithm=self._algorithm)
        except Exception as _:
            return None

    def generate_access_token(self, payload: dict) -> str:
        try:
            payload.update(self._primary_payload_data)
            return jwt.encode(payload, self._private_key, algorithm=self._algorithm)
        except Exception as error:
            return None

    def decode(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self._public_key, algorithms=[
                self._algorithm
            ], audience=self._audience, issuer=self._issuer)
            return payload
        except jwt.ExpiredSignatureError as error:
            raise Exception(f"Token has expired. {error}")
        except jwt.InvalidTokenError as error:
            raise Exception(f"Invalid token. {error}")
