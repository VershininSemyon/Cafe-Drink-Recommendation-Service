
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .tasks import send_registration_email, send_welcome_email
from . import registration_service
from . import exceptions


@api_view(['POST'])
@permission_classes([AllowAny])
def initiate_registration(request):
    try:
        token = registration_service.initiate_registration(request.data)
    except exceptions.InvalidRegistrationDataError as e:
        return Response(
            e.args[0] if e.args else {"error": "Invalid data"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    send_registration_email.delay(
        email=token.email,
        username=token.username,
        token=str(token.token)
    )

    return Response({
        'message': 'Письмо с подтверждением отправлено на ваш email',
        'email': token.email
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def complete_registration(request, token):
    try:
        registration, user_data = registration_service.complete_registration(token)

    except exceptions.LinkDoesNotExistError:
        return Response({
            'error': 'Ссылка не существует.'
        }, status=status.HTTP_404_NOT_FOUND)

    except exceptions.LinkIsExpiredError:
        return Response({
            'error': 'Ссылка устарела. Запросите новое письмо.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    except exceptions.UserAlreadyExistsError:
        return Response({
            'error': 'Пользователь уже зарегистрировался.'
        }, status=status.HTTP_400_BAD_REQUEST)

    send_welcome_email.delay(
        user_username=registration.username, 
        user_email=registration.email
    )

    return Response({
        'message': 'Регистрация успешно завершена',
        'user': user_data
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def resend_registration_email(request):
    try:
        old_registration = registration_service.resend_registration_email(request.data.get('email'))

    except exceptions.EmailIsRequiredError:
        return Response({
            'error': 'Email обязателен'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    except exceptions.UserIsAlreadyRegisteredError:
        return Response({
            'error': 'Пользователь с таким email уже зарегистрирован'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    except exceptions.UserHasNoOldRegistrationLinksError:
        return Response({
            'error': 'Не найдена незавершённая регистрация для этого email'
        }, status=status.HTTP_404_NOT_FOUND)

    send_registration_email.delay(
        email=old_registration.email,
        username=old_registration.username,
        token=str(old_registration.token)
    )
    
    return Response({
        'message': 'Письмо отправлено повторно'
    }, status=status.HTTP_200_OK)
