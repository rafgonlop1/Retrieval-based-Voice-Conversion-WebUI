import traceback

import gradio as gr


def load_faq():
    try:
        with open("docs/faq.md", "r", encoding="utf8") as f:
            info = f.read()
        return gr.Markdown(value=info)
    except Exception as e:
        print(e)
        return gr.Markdown(traceback.format_exc())
