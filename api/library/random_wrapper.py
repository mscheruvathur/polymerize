import random
import string

class RandomWrapper:
    @staticmethod
    def generate_with_number(length):
        return random.randint(0, length)

    @staticmethod
    def generate_with_calpha_numeric(length):
        calpha_numeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        key = ""
        for i in range(length):
            key += random.choice(calpha_numeric)
        return key

    @staticmethod
    def generate_with_salpha_numeric(length):
        salpha_numeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        key = ""
        for i in range(length):
            key += random.choice(salpha_numeric)
        return key

def random_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_user_id_generator(instance):
    user_new_id= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(user_id=user_new_id).exists()
    if qs_exists:
        return unique_user_id_generator(instance)
    return user_new_id
