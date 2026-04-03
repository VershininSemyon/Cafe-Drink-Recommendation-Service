
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_registration_email(email: str, username: str, token: str) -> str:
    registration_url = f"{settings.FRONTEND_URL}/complete-registration/{token}"
    
    subject = 'Завершение регистрации в Cafe Drink Recommendation Service'
    message = f'''
        Здравствуйте!

        Для завершения регистрации на платформе Cafe Drink Recommendation Service перейдите по ссылке:
        {registration_url}

        Ссылка действительна в течение 24 часов.

        Ваши данные для входа:
        Логин: {username}

        Если вы не регистрировались на нашем сайте, просто проигнорируйте это письмо.

        С уважением,
        Команда Cafe Drink Recommendation Service
    '''
    
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )
    
    return f"Сообщение о подтверждении регистрации отправлено пользователю на почту {email}"


@shared_task
def send_welcome_email(user_username: str, user_email: str):
    subject = 'Добро пожаловать в Cafe Drink Recommendation Service!'
    message = f'''
        Уважаемый(ая) {user_username}!

        Добро пожаловать в Cafe Drink Recommendation Service!

        Ваш email успешно подтверждён и регистрация завершена.

        Для входа в систему используйте ваш логин: {user_username}

        Мы рады видеть вас в нашем сообществе! Если у вас возникнут вопросы 
        или потребуется помощь, не стесняйтесь обращаться в службу поддержки.

        Желаем успешной работы с нашей системой!

        С уважением,
        Команда Cafe Drink Recommendation Service
    '''
    
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
        fail_silently=False,
    )
    
    return f"Приветственное сообщение отправлено пользователю на почту {user_email}"
