from accounts.models import Customer


def create_customer(user, phone_number):
    return Customer.objects.create(user=user, phone_number=phone_number)
