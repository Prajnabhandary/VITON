# DM-VTON: Virtual Try-On

## Table of Contents

- [Introduction](#introduction)
  
- [Solution Architecture](#solution-architecture)
  
- [Tools/Models Used](#toolsmodels-used)
  
- [Example](#example)


## Introduction

This application allows users to visualize how different clothing items will look on them, leveraging advanced image processing and machine learning techniques. By simply uploading images of themselves and the clothing item, users can see a realistic virtual try-on image. This document provides a comprehensive overview of the solution architecture, tools and models used, and detailed examples of input and output.

## Solution Architecture

The solution architecture of DM-VTON consists of an end-to-end pipeline designed to generate virtual try-on images efficiently. Below is the architecture diagram:

![Solution Architecture Diagram](https://raw.githubusercontent.com/KiseKloset/DM-VTON/assets/model_diagram.png)

1. **User Uploads**:
    - The user uploads two images: an original image of themselves and an image of the clothing item they wish to try on.

2. **Preprocessing**:
    - **Resizing**: Both images are resized to a standard dimension (192x256) to ensure consistency and optimal performance during the try-on process.
    - **Masking**: A mask of the clothing item is generated using the `rembg` tool, which helps in isolating the clothing item from its background.

3. **Virtual Try-On**:
    - **Pipeline Initialization**: A deep learning pipeline, `DMVTONPipeline`, is initialized with pre-trained models for warping the clothing item to fit the user's body shape and for generating the final try-on image.
    - **Image Generation**: The pipeline takes the resized original image, the resized clothing image, and the generated mask as inputs to produce a realistic virtual try-on image. The result is saved and displayed to the user.

## Tools/Models Used

- **Streamlit**: Creates an interactive web interface for uploading images and displaying results.

- **PIL (Pillow)**: Opens, manipulates, and saves images.

- **rembg**: Removes the background from the clothing image, creating a mask to isolate the clothing item.

- **torch**: Provides tools for building and deploying neural networks.

- **tqdm**:Displays progress bars to make processing steps transparent to the user.

- **cupy**: Accelerates computations using CUDA-based GPU computing.

- **thop**: Computes the number of operations in neural networks for profiling.

- **torchvision**: Includes popular datasets, model architectures, and image transformations for computer vision tasks.

- **utils.general**: Contains utility functions for profiling, logging, and warming up the model.

- **utils.metrics**: Calculates evaluation metrics like FID (Fréchet Inception Distance) and LPIPS (Learned Perceptual Image Patch Similarity).

- **utils.torch_utils**: Provides utility functions for selecting devices and optimizing performance.

- **SingleImageDataset**: Loads single image data for the virtual try-on process.

- **DMVTONPipeline**: Integrates different stages of the virtual try-on process, including image warping and generation.


## Example

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


- **Output Image**:
  ![Example Output](https://github.com/Prajnabhandary/VITON/blob/main/Inpainting/Img_4.png)


Ensure you have a CUDA-compatible GPU and the necessary drivers installed for the best performance.


