# DM-VTON: Virtual Try-On

## Table of Contents

- [Introduction](#introduction)
  
- [Solution Architecture](#solution-architecture)
  
- [Tools/Models Used](#toolsmodels-used)

- [Installation](#installation-used)
  
- [Example](#example)


## Introduction

This application allows users to visualize how different clothing items will look on them, leveraging advanced image processing and machine learning techniques. By simply uploading images of themselves and the clothing item, users can see a realistic virtual try-on image. This document provides a comprehensive overview of the solution architecture, tools and models used, and detailed examples of input and output.

## Solution Architecture

The solution architecture of DM-VTON consists of an end-to-end pipeline designed to generate virtual try-on images efficiently. Below is the architecture diagram:

![Solution Architecture Diagram]()

1. **User Uploads**:
    - The user uploads two images: an original image of themselves and an image of the clothing item they wish to try on.

2. **Preprocessing**:
    - **Resizing**: Both images are resized to a standard dimension (192x256) to ensure consistency and optimal performance during the try-on process.
    - **Masking**: A mask of the clothing item is generated using the `rembg` tool, which helps in isolating the clothing item from its background.

3. **Virtual Try-On**:
    - **Pipeline Initialization**: A deep learning pipeline, `DMVTONPipeline`, is initialized with pre-trained models for warping the clothing item to fit the user's body shape and for generating the final try-on image.
    - **Image Generation**: The pipeline takes the resized original image, the resized clothing image, and the generated mask as inputs to produce a realistic virtual try-on image. The result is saved and displayed to the user.

## Tools and Models Used

### Masking: `rembg`
- **Purpose**: Removes the background from images.
- **Function**: Utilizes deep learning to distinguish and eliminate the background, isolating the foreground object.
- **Use Case**: Useful for photo editing, object isolation, and background replacement.

### Warping: `MobileAFWM` (Mobile Affine Flow Warping Module)
- **Purpose**: Aligns the clothing image with the person image.
- **Function**: Uses affine transformations to estimate a flow field that aligns one image to another.
- **Use Case**: Employed in image registration, optical flow, and augmented reality.

### Blending: `MobileNetV2_unet`
- **Purpose**: Synthesizes and blends images.
- **Function**: Combines features from multiple images using a U-Net architecture to generate a cohesive output image.
- **Use Case**: Applied in image inpainting, style transfer, and image translation.


## Installation

To set up the project, follow the steps below:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/DM-VTON.git
   cd DM-VTON
   ```

2. **Install the required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application**:
   ```sh
   streamlit run app.py
   ```

- **Open your web browser**: Navigate to `http://localhost:8501`.

- **Upload an image**: Use the file uploader provided in the web interface to upload an image you want to process.

- **Generate the inpainted image**: Click the "Generate" button to create the inpainted image. The application will display the original and the inpainted images side by side, allowing you to compare the results and see the transformation instantly.

## Example

- **Output Image**:
  ![Example Output]()


Ensure you have a CUDA-compatible GPU and the necessary drivers installed for the best performance.


