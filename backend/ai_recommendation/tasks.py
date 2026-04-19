
from celery import shared_task
from drinks.models import Drink
from .models import Answer, Message

from .llm_api_service import get_llm_client, create_prompt
from .redis_client import get_redis


@shared_task
def process_message(
    message_text: str,
    drink_filters: dict,
    message_id: str,
    dialog_id: str,
    user_id: int
):
    drinks = (
        Drink.objects.all()
        if not drink_filters
        else Drink.objects.filter(**drink_filters)
    )
    drinks = "\n".join([drink.convert_to_string() for drink in drinks])

    key = f"user:{user_id}->dialog_id:{dialog_id}"
    ttl = 3600 * 24 * 3 # 3 дня

    redis = get_redis()
    history = redis.lrange(key, 0, -1)

    prompt = create_prompt(message_text, drink_filters, drinks, history)
    llm_client = get_llm_client()

    answer = llm_client.send_request_to_llm(prompt)
    message = Message.objects.get(id=message_id)
    Answer.objects.create(
        text=answer,
        message=message
    )

    redis.lpush(key, message_text)
    redis.lpush(key, answer)
    redis.expire(key, ttl)

    return answer, prompt
