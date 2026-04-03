
import uuid

from . import exceptions
from .models import RegistrationToken, User
from .serializers import RegistrationInitSerializer, UserSerializer
from django.contrib.auth.hashers import make_password


def initiate_registration(request_data: dict) -> RegistrationToken:
    serializer = RegistrationInitSerializer(data=request_data)

    if not serializer.is_valid():
        raise exceptions.InvalidRegistrationDataError(serializer.errors)
    
    registration_token = RegistrationToken.objects.create(
        email=serializer.validated_data['email'],
        username=serializer.validated_data['username'],
        password=make_password(serializer.validated_data['password']),
        token=uuid.uuid4()
    )

    return registration_token


def complete_registration(token: str) -> tuple[RegistrationToken, dict]:
    try:
        registration = RegistrationToken.objects.get(token=token)
    except RegistrationToken.DoesNotExist:
        raise exceptions.LinkDoesNotExistError
    
    if registration.is_expired():
        raise exceptions.LinkIsExpiredError
    
    if any([
        User.objects.filter(email=registration.email).exists(),
        User.objects.filter(username=registration.username).exists()
    ]):
        registration.is_used = True
        registration.save()

        raise exceptions.UserAlreadyExistsError
    
    user = User.objects.create(
        username=registration.username,
        email=registration.email,
        password=registration.password
    )
    user.email_verified = True
    user.save()
    
    registration.is_used = True
    registration.save()
    
    return registration, UserSerializer(user).data


def resend_registration_email(email: str):
    if not email:
        raise exceptions.EmailIsRequiredError

    if User.objects.filter(email=email).exists():
        raise exceptions.UserIsAlreadyRegisteredError
    
    try:
        old_registration = RegistrationToken.objects.filter(
            email=email, 
            is_used=False
        ).latest('created_at')

        return old_registration
        
    except RegistrationToken.DoesNotExist:
        raise exceptions.UserHasNoOldRegistrationLinksError
