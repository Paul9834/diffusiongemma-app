# DiffusionGemma App

Interfaz web local construida con **Gradio** para interactuar con el modelo `google/diffusiongemma-26B-A4B-it` a través de un servidor **vLLM** local. Diseñada para generación de texto en español con control sobre objetivos, estilos y parámetros de inferencia. [cite:3][cite:4]

## Características

- Conecta a un servidor vLLM local mediante una API compatible con OpenAI. [cite:3][cite:4]
- Permite elegir objetivo de escritura y estilo desde una interfaz Gradio. [cite:4]
- Expone controles de `temperature` y `max_tokens` para ajustar la generación. [cite:4]
- Usa variables de entorno para configurar host, puerto, modelo y endpoint del servidor. [cite:3][cite:4]
- Responde en español con un prompt base orientado a escritura profesional. [cite:4]

## Estructura del proyecto

```text
diffusiongemma-app/
├── app/
│   ├── client.py
│   ├── config.py
│   ├── main.py
│   ├── prompts.py
│   └── ui.py
├── .env.example
├── main.py
└── requirements.txt
```

- `app/main.py`: punto de entrada real para lanzar la UI. [cite:4]
- `app/client.py`: cliente que envía prompts al servidor vLLM usando el SDK de OpenAI. [cite:4]
- `app/config.py`: carga configuración desde `.env`. [cite:4]
- `app/prompts.py`: define el system prompt y compone el prompt final del usuario. [cite:4]
- `app/ui.py`: construye la interfaz de Gradio. [cite:4]
- `main.py` en la raíz: archivo placeholder generado por PyCharm, no parece formar parte del flujo principal. [cite:2]

## Requisitos

- Python 3.10 o superior.
- Un servidor vLLM corriendo localmente.
- El modelo `google/diffusiongemma-26B-A4B-it` cargado en ese servidor. [cite:3]

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Dependencias declaradas actualmente: `gradio`, `openai`, `python-dotenv` y `pydantic`. [cite:3]

## Configuración

Copia `.env.example` a `.env` y ajusta los valores si hace falta:

```env
VLLM_BASE_URL=http://127.0.0.1:8000/v1
VLLM_API_KEY=EMPTY
VLLM_MODEL_ID=google/diffusiongemma-26B-A4B-it
APP_HOST=127.0.0.1
APP_PORT=7860
```

| Variable | Descripción | Valor por defecto |
|---|---|---|
| `VLLM_BASE_URL` | URL base del servidor vLLM | `http://127.0.0.1:8000/v1` |
| `VLLM_API_KEY` | API key usada por el cliente | `EMPTY` |
| `VLLM_MODEL_ID` | Modelo servido por vLLM | `google/diffusiongemma-26B-A4B-it` |
| `APP_HOST` | Host de la interfaz | `127.0.0.1` |
| `APP_PORT` | Puerto de la interfaz | `7860` |

Estos valores están definidos en `.env.example` y también tienen fallback en `app/config.py`. [cite:3][cite:4]

## Ejecución

```bash
python -m app.main
```

La app levanta una interfaz Gradio usando `settings.host` y `settings.port`. [cite:4]

## Flujo interno

1. El usuario escribe un prompt en la UI. [cite:4]
2. La app combina ese texto con un objetivo y estilo seleccionados. [cite:4]
3. El cliente envía los mensajes al endpoint compatible con OpenAI del servidor vLLM. [cite:4]
4. La respuesta del modelo se muestra en el cuadro de salida. [cite:4]

## Mejoras sugeridas

- Reemplazar el `main.py` de la raíz por un launcher útil o eliminarlo para evitar confusión. [cite:2][cite:4]
- Añadir manejo de errores más específico para timeout, conexión y respuestas vacías del modelo.
- Incluir instrucciones para levantar vLLM en local dentro del README.
- Agregar screenshots o ejemplos de prompts y salidas.
- Añadir pruebas básicas para validar configuración y conectividad.

## Licencia

Define aquí la licencia del proyecto si vas a publicarlo o compartirlo.
