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

## Workflow

1. **Upload Images**: Users interact with a web interface to upload two images: one of the person and one of the clothing item they wish to try on. The interface supports common image formats such as JPG and PNG.
   
2. **Preprocessing**: 
   - **Resize Images**: The uploaded images are resized to a standard resolution suitable for processing. This ensures consistency and improves the efficiency of the subsequent steps.
   - **Background Removal**: The `rembg` tool is used to remove the background from the clothing image. This step isolates the garment, creating a mask that highlights the clothing item and discards any unwanted background elements.

3. **Warping**: The preprocessed clothing image and mask are fed into the `MobileAFWM` (Mobile Affine Flow Warping Module) model. This model aligns the clothing image with the person image by estimating a flow field that accurately deforms the clothing to match the shape and pose of the person. This step ensures that the garment fits naturally on the person's body.

4. **Blending**: The aligned clothing image, along with the person image, is passed to the `MobileNetV2_unet` model. This blending model synthesizes the final output by combining features from both images. It ensures a seamless integration of the clothing onto the person, resulting in a realistic try-on effect.

5. **Display**: The final try-on image, along with the original person image and the clothing image, are displayed on the web interface. This allows users to visually compare and evaluate the virtual try-on result directly in their browser.

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


## Example

- **Output Image**:
  ![Example Output]()


Ensure you have a CUDA-compatible GPU and the necessary drivers installed for the best performance.


