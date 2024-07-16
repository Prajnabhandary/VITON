# Virtual Try-On (Inpainting)

This project provides a virtual try-on experience by leveraging background removal and inpainting techniques. It uses the `rembg` library for background removal and the `diffusers` library for inpainting with Stable Diffusion. The application is built with Streamlit to provide an easy-to-use web interface.

### What we have?
We have an end-to-end pipeline/framework for generating virtual try-on images by removing backgrounds and using inpainting techniques. This approach can be adapted to various use cases involving image processing and manipulation.

<div id="top"></div>
<h3 align="center">Virtual Try-On Architecture and How to Use It</h3>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#work-flow">Work Flow</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#code-explanation">Code Explanation</a></li>
    <li><a href="#dependencies">Dependencies</a></li>
  </ol>
</details>

<a name="readme-top"></a>
## Work Flow
The below image shows the end-to-end pipeline of the virtual try-on framework:

## Installation

1. Clone the repository:

   git clone https://github.com/your-org/virtual-try-on.git
   cd virtual-try-on


2. Install the required dependencies:

   pip install -r requirements.txt


3. Ensure you have the necessary model for inpainting downloaded:

   from diffusers import AutoPipelineForInpainting
   pipeline = AutoPipelineForInpainting.from_pretrained(
       "runwayml/stable-diffusion-inpainting", torch_dtype=torch.float16, variant="fp16", safety_checker=None,
       requires_safety_checker=False
   ).to("cuda")


## Usage

1. Run the Streamlit application:

   streamlit run app.py


2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload an image using the file uploader.

4. Click the "Generate" button to create the inpainted image.

## Code Explanation

### `process_image`

The `process_image` function handles the image processing workflow:
- Removes the background using the `rembg` library.
- Creates and inverts the mask.
- Loads the Stable Diffusion inpainting model.
- Generates the inpainted image using a specified prompt.
- Saves the inpainted image to the specified output path.

### Streamlit Application

The Streamlit application:
- Displays the original uploaded image.
- Calls the `process_image` function to generate the inpainted image.
- Displays the inpainted image next to the original image.

## Dependencies

- `streamlit`
- `rembg`
- `Pillow`
- `torch`
- `diffusers`

Ensure you have a CUDA-compatible GPU and the necessary drivers installed for the best performance.