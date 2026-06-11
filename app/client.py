from openai import OpenAI
from app.config import settings
from app.prompts import SYSTEM_PROMPT, build_user_prompt

client = OpenAI(
    base_url=settings.base_url,
    api_key=settings.api_key,
)

def generate_text(prompt: str, objective: str, style: str, temperature: float, max_tokens: int) -> str:
    user_prompt = build_user_prompt(prompt, objective, style)
    response = client.chat.completions.create(
        model=settings.model_id,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()
