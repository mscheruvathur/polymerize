from api.models import AuthCode
from api.library.random_wrapper import RandomWrapper
from datetime import datetime, timezone, timedelta


class UserController :

    def __init__(self) -> None:
        pass

    def create_user ():
        try:
            pass
        except Exception as e:
            raise e

    def login() :
        try:
            pass
        except Exception as e: 
            raise e

    def update():
        try:
            pass
        except Exception as e:
            raise e
    
    def get():
        try:
            pass
        except Exception as e:
            raise e
    
    def delete():
        try:
            pass
        except Exception as e:
            raise e
    
    def generate_auth_code(self, user = None, admin = None, administrator = None):
        try:
            auth_code = RandomWrapper.generate_with_salpha_numeric(length=10)
            if user:
                auth_code_instance = AuthCode.objects.create(
                    auth_code=auth_code,
                    user=user,
                    is_used=False,
                    expiration = datetime.now(tz=timezone.utc) + timedelta(minutes=2)
                )
                auth_code_instance.save()
                return auth_code
            if admin:
                auth_code_instance = AuthCode.objects.create(
                    auth_code=auth_code,
                    admin=admin,
                    is_used=False,
                    expiration = datetime.now(tz=timezone.utc) + timedelta(minutes=2)
                )
                auth_code_instance.save()
                return auth_code
            if administrator:
                auth_code_instance = AuthCode.objects.create(
                    auth_code=auth_code,
                    administrator=administrator,
                    is_used=False,
                    expiration = datetime.now(tz=timezone.utc) + timedelta(minutes=2)
                )
                auth_code_instance.save()
                return auth_code
        except Exception as e:
            raise e

    def expir_auth_code(self, auth_code):
        try:
            auth = AuthCode.objects.get(auth_code=auth_code)
            auth.is_used = True
            auth.save()
        except Exception as e:
            raise e

    def get_auth_code(self, auth_code):
        try:
            return AuthCode.objects.get(auth_code=auth_code, is_used=False, is_active=True)
        except AuthCode.DoesNotExist:
            return False

    def verify_auth_code(self, auth_code):
        try:
            import pytz
            utc=pytz.UTC
            instance = AuthCode.objects.get(auth_code=auth_code)
            created = instance.expiration.replace(tzinfo=utc)
            current = datetime.now(tz=timezone.utc).replace(tzinfo=utc)
            if created <= current:
                return False
            return instance
        except AuthCode.DoesNotExist:
            return False
        except Exception as e:
            raise e