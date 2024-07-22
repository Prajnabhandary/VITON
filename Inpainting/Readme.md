
# Virtual Try-On

This project provides a virtual try-on experience by leveraging background removal and inpainting techniques. It uses the `rembg` library for background removal and the `diffusers` library for inpainting with Stable Diffusion. The application is built with Streamlit to provide an easy-to-use web interface.

## Table of Contents
1. [Introduction](#introduction)
   
2. [Solution Architecture](#solution-architecture)
   
3. [Tools/Models Used](#toolsmodels-used)

4. [Installation](#installation)

5. [Results](#results)

## Introduction

The Virtual Try-On (Inpainting) project is designed to offer a seamless and realistic virtual try-on experience. By utilizing advanced image processing techniques, we can remove the background from an image and apply inpainting to generate a high-quality visualization of the subject in various settings or outfits. This technology can be applied to online shopping, virtual fitting rooms, and other domains where visual representation is crucial. Imagine being able to see how a particular dress or outfit looks on you without ever having to leave your home. Our solution aims to revolutionize the way we shop online, making it more interactive and engaging.

## Solution Architecture

![Solution Architecture Diagram](https://github.com/Prajnabhandary/VITON/blob/main/Inpainting/Inpainting_arch.jpg)

The solution architecture consists of an end-to-end pipeline for generating virtual try-on images. The process begins with background removal using the `rembg` library, which efficiently isolates the subject from the background. The next step involves inpainting the isolated subject into a new context or environment using the `diffusers` library and the Stable Diffusion model. This architecture is highly adaptable and can be extended to various image processing and manipulation applications. By breaking down the process into manageable steps, we ensure a smooth and efficient workflow that produces high-quality results every time.

## Tools/Models Used

### Background Removal: rembg

The `rembg` library is used for removing the background from images, leaving only the subject. This step is crucial for isolating the subject and preparing it for inpainting.

The `rembg` library is an open-source tool designed for removing the background from images. It uses deep learning models to identify and isolate the main subject in an image, effectively separating it from the background. This is particularly useful in applications such as virtual try-on, where we need to place the subject in different environments or backgrounds.

### Inpainting: diffusers with Stable Diffusion

The `diffusers` library with the Stable Diffusion model is used to seamlessly blend the subject into a new background or environment. This allows us to place the subject in various settings, providing a realistic preview of how the subject would look in different contexts.

Stable Diffusion is a state-of-the-art generative model for image inpainting. The model is designed to fill in missing parts of an image in a way that is coherent and visually appealing. By using the `diffusers` library, we can leverage this powerful model to seamlessly blend subjects into new backgrounds or environments, creating realistic previews.

By combining `rembg` for background removal and Stable Diffusion for inpainting, we create a robust system for generating high-quality virtual try-on previews. The subject can be placed in various settings, providing a realistic and immersive experience.

## Installation

### Prerequisites

 **Ensure you have Python 3.8 installed. Then, create and activate a virtual environment named dmvton_env**:
   ```sh
   python3.8 -m venv dmvton_env
   source dmvton_env/bin/activate
   ```
To set up the project, follow the below steps:

1. **Clone the repository:** Open your terminal and run the following command to clone the repository to your local machine.

    ```sh
    git clone https://github.com/your-org/virtual-try-on.git
    cd virtual-try-on
    ```

2. **Install the required dependencies:** Navigate to the project directory and install all the necessary dependencies by running the following command.

    ```sh
    pip install -r requirements.txt
    ```


3. To use the application, follow these steps:

- **Run the Streamlit application:** Open your terminal and navigate to the project directory. Run the following command to start the Streamlit application.

    ```sh
    streamlit run app.py
    ```

- **Open your web browser:** Once the Streamlit application is running, open your web browser and navigate to `http://localhost:8501`.

## Results

- **Output Image 1:**
  ![Example Input]()

### Platform GPU and Memory Configurations for Inpainting

1. **Google Colab**: Typically provides access to NVIDIA Tesla K80, T4, P4, or P100 GPUs with memory sizes of 12 GB GDDR5 (K80), 16 GB GDDR6 (T4), 8 GB GDDR5 (P4), and 16 GB HBM2 (P100).
2. **Kaggle**: Offers NVIDIA Tesla P100 GPUs with 16 GB HBM2 memory.
3. **AWS Medium Instance**: Includes instances like `g4dn.xlarge` with NVIDIA T4 (16 GB GDDR6, 16 GB system memory) and `p2.xlarge` with NVIDIA K80 (12 GB GDDR5, 61 GB system memory).
