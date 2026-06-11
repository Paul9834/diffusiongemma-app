SYSTEM_PROMPT = """Eres un asistente de escritura profesional.
Tu trabajo es producir texto natural, claro, útil y no genérico.
Responde en español, con tono humano y precisión.
"""

def build_user_prompt(prompt: str, objective: str, style: str):
    return f"""Objetivo: {objective}
Estilo: {style}

Instrucción del usuario:
{prompt}
"""
