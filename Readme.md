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

1. **Upload Images**: Users needs to upload two images, one image of the person and another of the clothing item they intend to try on. The interface supports common image formats such as JPG and PNG.
   
2. **Preprocessing**: 
   - **Resize Images**: The uploaded images are resized to a standard resolution suitable for processing. This ensures consistency and efficiency of the subsequent steps.
   - **Background Removal**: The `rembg` tool is used to remove the background from the clothing image. This step isolates the garment, creating a mask that highlights the clothing item and discards any unwanted background elements.

3. **Warping**: The preprocessed clothing image and mask are fed into the `MobileAFWM` (Mobile Affine Flow Warping Module) model. This model aligns the clothing image with the person image by estimating a flow field that accurately deforms the clothing to match the shape and pose of the person. This step ensures that the garment fits naturally on the person's body.

4. **Blending**: The aligned clothing image, along with the person image, is passed to the `MobileNetV2_unet` model. This blending model synthesizes the final output by combining features from both images. It ensures a seamless integration of the clothing onto the person, resulting in a realistic try-on effect.

5. **Display**: The final try-on image, along with the original person image and the clothing image, are displayed on the web interface. This allows users to visually compare and evaluate the virtual try-on result.

## Tools and Models Used

### Background Removal with `rembg`

The `rembg` tool is utilized to remove the background from images with high precision. Leveraging advanced deep learning algorithms, `rembg` accurately distinguishes and eliminates the background, isolating the foreground object effectively. This process is crucial for ensuring that only the clothing item remains in the image, free from any extraneous background elements. This capability is particularly useful for applications such as:

- Photo editing
- Object isolation
- Background replacement

By achieving clean and precise object separation, `rembg` enhances the quality and usability of images for various applications.

### Image Warping with `MobileAFWM` (Mobile Affine Flow Warping Module)

The `MobileAFWM` model is essential for aligning the clothing image with the person image. By employing affine transformations, this model estimates a flow field that dictates how each pixel in the clothing image should be moved to perfectly align with the person’s pose and shape. This warping process ensures that the garment fits naturally onto the person’s body. The technique is widely used in:

- Image registration
- Optical flow
- Augmented reality applications

where precise alignment between images is necessary. The `MobileAFWM` model enhances the realism and accuracy of the virtual try-on experience by ensuring that the clothing fits seamlessly onto the person's image.

### Image Blending with `MobileNetV2_unet`

The `MobileNetV2_unet` model is responsible for synthesizing and blending images to create the final try-on result. Utilizing a U-Net architecture, this model combines features from both the person image and the warped clothing image. It excels at generating cohesive and realistic output images by blending the input images seamlessly. The applications of this model extend to:

- Image inpainting
- Style transfer
- Image translation

making it a versatile tool for various image synthesis tasks. By ensuring smooth and realistic blending of images, `MobileNetV2_unet` enhances the overall quality and visual appeal of the virtual try-on results.


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


