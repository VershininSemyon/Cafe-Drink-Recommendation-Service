
from config.config import settings
from openai import OpenAI


class LlmApiClient:
    def __init__(
            self, 
            api_key: str, 
            base_url: str = "https://openrouter.ai/api/v1", 
            model: str = "arcee-ai/trinity-large-preview:free"
        ):
        self._model = model
        self._api_key = api_key

        self._client = OpenAI(
            base_url=base_url,
            api_key=api_key,
        )

    @property
    def model(self) -> str:
        return self._model

    @property
    def api_key(self) -> str:
        return self._api_key

    def send_request_to_llm(self, prompt: str):
        try:
            completion = self._client.chat.completions.create(
                model=self._model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            return completion.choices[0].message.content
        except Exception as e:
            return f"Ошибка ответа: {e}"


def get_llm_client() -> LlmApiClient:
    return LlmApiClient(api_key=settings.LLM_API_KEY)


def create_prompt(
    message_text: str,
    drink_filters: str,
    drinks: str,
    history: str
) -> str:
    prompt = f"""
        Ты - кофейный эксперт.
        Вот пожелания пользователя: {message_text} и фильтры: {drink_filters}.
        Вот история общения для понимания контекста {history} и подходящие напитки: {drinks}.
        Посоветуй какие-нибудь напитки и дай комментарии к каждому.
    """

    return prompt
