import gradio as gr
from rembg import remove
from PIL import Image
import os

def process_image(input_image):
    # Remove background
    output_image = remove(input_image)
    return output_image

# Create the Gradio interface
with gr.Blocks(title="Background Removal App") as demo:
    gr.Markdown("# Add your image to remove the background")
    
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(label="Input Image", type="pil")
            process_btn = gr.Button("Remove Background")
        
        with gr.Column():
            output_image = gr.Image(label="Output Image")
    
    process_btn.click(
        fn=process_image,
        inputs=input_image,
        outputs=output_image
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(share=True) 