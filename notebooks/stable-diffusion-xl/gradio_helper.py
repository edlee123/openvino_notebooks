import gradio as gr
from diffusers.utils import load_image
import numpy as np


# TODO Consider reusing make_demo_segmind_vegart
def make_demo_sd_xl_text2image(pipeline):
    def generate_from_text(text, seed, num_steps):
        result = pipeline(
            text,
            num_inference_steps=num_steps,
            generator=np.random.RandomState(seed),
            height=512,
            width=512,
        ).images[0]
        return result

    with gr.Blocks() as demo:
        with gr.Column():
            positive_input = gr.Textbox(label="Text prompt")
            with gr.Row():
                seed_input = gr.Number(precision=0, label="Seed", value=42, minimum=0)
                steps_input = gr.Slider(label="Steps", value=10)
                btn = gr.Button()
            out = gr.Image(label="Result", type="pil", width=512)
            btn.click(generate_from_text, [positive_input, seed_input, steps_input], out)
            gr.Examples(
                [
                    ["cute cat 4k, high-res, masterpiece, best quality, soft lighting, dynamic angle", 999, 20],
                    [
                        "underwater world coral reef, colorful jellyfish, 35mm, cinematic lighting, shallow depth of field,  ultra quality, masterpiece, realistic",
                        89,
                        20,
                    ],
                    [
                        "a photo realistic happy white poodle dog ​​playing in the grass, extremely detailed, high res, 8k, masterpiece, dynamic angle",
                        1569,
                        15,
                    ],
                    [
                        "Astronaut on Mars watching sunset, best quality, cinematic effects,",
                        65245,
                        12,
                    ],
                    [
                        "Black and white street photography of a rainy night in New York, reflections on wet pavement",
                        48199,
                        10,
                    ],
                ],
                [positive_input, seed_input, steps_input],
            )
    return demo


def make_demo_sd_xl_image2image(pipeline):
    load_image("https://huggingface.co/datasets/optimum/documentation-images/resolve/main/intel/openvino/sd_xl/castle_friedrich.png").resize((512, 512)).save(
        "castle_friedrich.png"
    )

    def generate_from_image(text, image, seed, num_steps):
        result = pipeline(
            text,
            image=image,
            num_inference_steps=num_steps,
            generator=np.random.RandomState(seed),
        ).images[0]
        return result

    with gr.Blocks() as demo:
        with gr.Column():
            positive_input = gr.Textbox(label="Text prompt")
            with gr.Row():
                seed_input = gr.Number(precision=0, label="Seed", value=42, minimum=0)
                steps_input = gr.Slider(label="Steps", value=10)
                btn = gr.Button()
            with gr.Row():
                i2i_input = gr.Image(label="Input image", type="pil")
                out = gr.Image(label="Result", type="pil", width=512)
            btn.click(
                generate_from_image,
                [positive_input, i2i_input, seed_input, steps_input],
                out,
            )
            gr.Examples(
                [
                    ["amazing landscape from legends", "castle_friedrich.png", 971, 60],
                    [
                        "Masterpiece of watercolor painting in Van Gogh style",
                        "cat.png",
                        37890,
                        40,
                    ],
                ],
                [positive_input, i2i_input, seed_input, steps_input],
            )

    return demo
