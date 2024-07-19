# DM-VTON: Virtual Try-On

## Table of Contents

- [Introduction](#introduction)
  
- [Solution Architecture](#solution-architecture)
  
- [Tools/Models Used](#toolsmodels-used)

- [Installation](#installation)
  
- [Results](#results)


## Introduction

This application allows users to visualize how different clothing items will look on them, leveraging advanced image processing and machine learning techniques. By simply uploading images of themselves and the clothing item, users can see a realistic virtual try-on image. This document provides a comprehensive overview of the solution architecture, tools and models used, and detailed examples of input and output.

## Solution Architecture

The solution architecture of DM-VTON consists of an end-to-end pipeline designed to generate virtual try-on images efficiently. Below is the architecture diagram:

![Solution Architecture Diagram](https://github.com/Prajnabhandary/VITON/blob/fix-issue/Inpainting/Img_11.jpg)

## Workflow

1. **Upload Images**: Users needs to upload two images, one image of the person and another of the clothing item they intend to try on. The interface supports common image formats such as JPG and PNG.
   
2. **Preprocessing**: 
   - **Resize Images**: The uploaded images are resized to a standard resolution suitable for processing. This ensures consistency and efficiency of the subsequent steps.
   - **Background Removal**: The `rembg` tool is used to remove the background from the clothing image. This step isolates the garment, creating a mask that highlights the clothing item and discards any unwanted background elements.

3. **Warping**: The preprocessed clothing image and mask are fed into the `MobileAFWM` (Mobile Affine Flow Warping Module) model. This model aligns the clothing image with the person image by estimating a flow field that accurately deforms the clothing to match the shape and pose of the person. This step ensures that the garment fits naturally on the person's body.

4. **Blending**: The aligned clothing image, along with the person image, is passed to the `MobileNetV2_unet` model. This blending model synthesizes the final output by combining features from both images. It ensures a seamless integration of the clothing onto the person, resulting in a realistic try-on effect.

5. **Display**: The final try-on image, along with the original person image and the clothing image, are displayed on the web interface. This allows users to visually compare and evaluate the virtual try-on result.

## Tools/Models Used

### 1. Background Removal with `rembg`

The `rembg` tool is used to remove backgrounds from images with high precision. By leveraging advanced deep learning algorithms, `rembg` accurately distinguishes and eliminates the background, isolating the foreground object effectively.

#### Applications:
- **Photo Editing**: Enhancing images by removing unwanted backgrounds.
- **Object Isolation**: Extracting specific objects from an image for further processing.
- **Background Replacement**: Changing the background of an image to suit different contexts.

### 2. Image Warping with `MobileAFWM` (Mobile Affine Flow Warping Module)

The `MobileAFWM` model is essential for aligning the clothing image with the person image. By employing affine transformations, this model estimates a flow field that dictates how each pixel in the clothing image should be moved to perfectly align with the person’s pose and shape. This warping process ensures that the garment fits naturally onto the person’s body.

#### Applications:
- **Image Registration**: Aligning images from different sources.
- **Optical Flow**: Tracking motion between frames.
- **Augmented Reality**: Ensuring precise alignment in AR applications.

### 3. Image Blending with `MobileNetV2_unet`

The `MobileNetV2_unet` model synthesizes and blends images to create the final try-on result. Utilizing a U-Net architecture, this model combines features from both the person image and the warped clothing image. It excels at generating cohesive and realistic output images by blending the input images seamlessly.

#### Applications:
- **Image Inpainting**: Filling in missing parts of an image.
- **Style Transfer**: Applying the style of one image to another.
- **Image Translation**: Converting images from one domain to another.


## Installation

### Prerequisites

To set up the project, follow the steps below:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/DM-VTON.git
   cd DM-VTON
   ```

2. **Ensure you have Python 3.8 installed. Then, create and activate a virtual environment named dmvton_env**:
   ```sh
   python3.8 -m venv dmvton_env
   source dmvton_env/bin/activate
   ```

3. **Install the required dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application**:
   ```sh
   streamlit run app.py
   ```

- **Open your web browser**: Navigate to `http://localhost:8501`.


## Results

- **Output Image 1**:
  ![Example Output](https://github.com/Prajnabhandary/VITON/blob/main/Inpainting/img_7.jpg)

- **Output Image 2**:
  ![Example Output](https://github.com/Prajnabhandary/VITON/blob/main/Inpainting/img_8.jpg)

  
Ensure you have a CUDA-compatible GPU and the necessary drivers installed for the best performance.
