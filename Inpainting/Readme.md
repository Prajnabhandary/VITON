
# Virtual Try-On (Inpainting)

This project provides a virtual try-on experience by leveraging background removal and inpainting techniques. It uses the `rembg` library for background removal and the `diffusers` library for inpainting with Stable Diffusion. The application is built with Streamlit to provide an easy-to-use web interface.

## Table of Contents
1. [Introduction](#introduction)
2. [Solution Architecture](#solution-architecture)
   1. [Solution Diagram](#solution-diagram)
   2. [Brief about the Architecture](#brief-about-the-architecture)
3. [Tools/Models Used](#toolsmodels-used)
4. [Example](#example)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Dependencies](#dependencies)

## Introduction

The Virtual Try-On (Inpainting) project is designed to offer a seamless and realistic virtual try-on experience. By utilizing advanced image processing techniques, we can remove the background from an image and apply inpainting to generate a high-quality visualization of the subject in various settings or outfits. This technology can be applied to online shopping, virtual fitting rooms, and other domains where visual representation is crucial.

## Solution Architecture

### Solution Diagram

![Solution Architecture Diagram](https://github.com/Prajnabhandary/VITON/blob/main/Inpainting/Arch_daigram.jpg)


### Brief about the Architecture

The solution architecture consists of an end-to-end pipeline for generating virtual try-on images. The process begins with background removal using the `rembg` library, which efficiently isolates the subject from the background. The next step involves inpainting the isolated subject into a new context or environment using the `diffusers` library and the Stable Diffusion model. This architecture is highly adaptable and can be extended to various image processing and manipulation applications.

## Tools/Models Used

- **Background Removal:** The `rembg` library is employed to accurately remove the background from images, leaving only the subject.
- **Inpainting:** The `diffusers` library with the Stable Diffusion model is used to seamlessly blend the subject into a new background or environment.
- **Web Interface:** Streamlit is utilized to create a user-friendly web interface, allowing users to easily upload images and view the inpainting results.

## Installation

To set up the project, follow these steps:

1. **Clone the repository:** Open your terminal and run the following command to clone the repository to your local machine.

    ```sh
    git clone https://github.com/your-org/virtual-try-on.git
    cd virtual-try-on
    ```

2. **Install the required dependencies:** Navigate to the project directory and install all the necessary dependencies by running the following command.

    ```sh
    pip install -r requirements.txt
    ```

3. **Download the necessary model for inpainting:** Run the following Python commands to download and set up the inpainting model.

    ```python
    from diffusers import AutoPipelineForInpainting
    pipeline = AutoPipelineForInpainting.from_pretrained(
        "runwayml/stable-diffusion-inpainting", torch_dtype=torch.float16, variant="fp16", safety_checker=None,
        requires_safety_checker=False
    ).to("cuda")
    ```

## Usage

To use the application, follow these steps:

1. **Run the Streamlit application:** Open your terminal and navigate to the project directory. Run the following command to start the Streamlit application.

    ```sh
    streamlit run app.py
    ```

2. **Open your web browser:** Once the Streamlit application is running, open your web browser and navigate to `http://localhost:8501`.

3. **Upload an image:** Use the file uploader provided in the web interface to upload an image you want to process.

4. **Generate the inpainted image:** Click the "Generate" button to create the inpainted image. The application will display the original and the inpainted images side by side.


### Example Output

- **Output 1:**
  ![Example Input](https://github.com/Prajnabhandary/VITON/blob/main/Inpainting/img_1.png)



## Dependencies

This project requires the following dependencies:

- `streamlit`: A framework for creating interactive web applications.
- `rembg`: A library for removing the background from images.
- `Pillow`: A Python Imaging Library that adds image processing capabilities.
- `torch`: A deep learning framework used for training and deploying machine learning models.
- `diffusers`: A library for using diffusion models, such as Stable Diffusion, for inpainting.

Ensure you have a CUDA-compatible GPU and the necessary drivers installed for the best performance.
