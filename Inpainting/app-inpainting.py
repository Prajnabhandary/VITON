import streamlit as st
from rembg import remove
from PIL import Image, ImageOps
import torch
import os
from diffusers import AutoPipelineForInpainting

# Function to remove background and generate image
def process_image(input_image, output_path):
    # Remove the background
    output_image = remove(input_image, alpha_threshold=0)

    # Create a mask
    mask = Image.new('L', output_image.size, 0)
    mask.paste(255, output_image.split()[-1])

    # Invert the colors in the mask (main object becomes black, background becomes white)
    inverted_mask = ImageOps.invert(mask)

    # Initialize generator
    generator = torch.Generator("cuda").manual_seed(-1)
    # Inpainting with diffusers
    pipeline = AutoPipelineForInpainting.from_pretrained(
        "runwayml/stable-diffusion-inpainting", torch_dtype=torch.float16, variant="fp16", safety_checker=None,
        requires_safety_checker=False
    ).to("cuda")

    # Specify prompt for inpainting
    prompt = "a mannequin posing for a picture weared a innerwear,ultrarealistic"

    # Generate inpainted image using inverted mask
    inpainted_image = pipeline(prompt=prompt, image=input_image, mask_image=inverted_mask, generator=generator).images[0]
    inpainted_image.save(output_path)

    return inpainted_image

# Streamlit app
def main():
    st.markdown("<h1 style='text-align: center;'>Virtual Try-On (Inpainting)</h1>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        # Display original image
        col1, col2 = st.columns(2) 

            # Display original image in the first column
        col1.subheader("**Original Image:**")
        col1.image(uploaded_file, use_column_width=True)

        # Button to generate inpainted image
        if st.button("Generate"):
            filename = os.path.splitext(uploaded_file.name)[0]

            # Specify the output path where you want to save the inpainted image
            output_path = f"/home/subhamkumar/cv/virtual_tryon/inpainting/Results/{filename}_vton.jpg"

            # Process the image and generate inpainted image
            inpainted_image = process_image(Image.open(uploaded_file), output_path)

            # Display inpainted image in the second column
            col2.subheader("**TryOn Image:**")
            col2.image(inpainted_image, use_column_width=True, width=True)

if __name__ == "__main__":
    main()
