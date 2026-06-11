import gradio as gr
from app.client import generate_text

OBJECTIVES = [
    "reescritura natural",
    "blog y SEO",
    "resumen técnico",
    "copy persuasivo",
    "explicación simple",
]

STYLES = [
    "claro y directo",
    "técnico y profesional",
    "casual y conversacional",
    "formal y académico",
]

def run(prompt, objective, style, temperature, max_tokens):
    if not prompt.strip():
        return "Escribe un prompt primero."
    try:
        return generate_text(
            prompt=prompt,
            objective=objective,
            style=style,
            temperature=temperature,
            max_tokens=int(max_tokens),
        )
    except Exception as e:
        return f"Error: {e}"

def build_ui():
    with gr.Blocks(title="DiffusionGemma Local") as demo:
        gr.Markdown("# DiffusionGemma Local")
        gr.Markdown("UI profesional conectada a un servidor vLLM local.")

        with gr.Row():
            prompt = gr.Textbox(
                lines=10,
                label="Prompt",
                placeholder="Pega aquí la instrucción o el texto base..."
            )

        with gr.Row():
            objective = gr.Dropdown(choices=OBJECTIVES, value=OBJECTIVES[0], label="Objetivo")
            style = gr.Dropdown(choices=STYLES, value=STYLES[0], label="Estilo")

        with gr.Row():
            temperature = gr.Slider(0.1, 1.5, value=0.7, step=0.05, label="Temperature")
            max_tokens = gr.Slider(64, 1024, value=256, step=32, label="Max tokens")

        btn = gr.Button("Generar", variant="primary")
        output = gr.Textbox(lines=14, label="Salida")

        btn.click(
            run,
            inputs=[prompt, objective, style, temperature, max_tokens],
            outputs=output,
        )

    return demo
