
# Virtual Try-On

This project provides a virtual try-on experience by leveraging background removal and inpainting techniques. It uses the `rembg` library for background removal and the `diffusers` library for inpainting with Stable Diffusion. The application is built with Streamlit to provide an easy-to-use web interface.

## Table of Contents
1. [Introduction](#introduction)
   
2. [Solution Architecture](#solution-architecture)
   
3. [Tools/Models Used](#toolsmodels-used)

4. [Example](#example)

## Introduction

The Virtual Try-On (Inpainting) project is designed to offer a seamless and realistic virtual try-on experience. By utilizing advanced image processing techniques, we can remove the background from an image and apply inpainting to generate a high-quality visualization of the subject in various settings or outfits. This technology can be applied to online shopping, virtual fitting rooms, and other domains where visual representation is crucial. Imagine being able to see how a particular dress or outfit looks on you without ever having to leave your home. Our solution aims to revolutionize the way we shop online, making it more interactive and engaging.

## Solution Architecture

![Solution Architecture Diagram](https://github.com/Prajnabhandary/VITON/blob/main/Inpainting/Arch_daigram.jpg)

The solution architecture consists of an end-to-end pipeline for generating virtual try-on images. The process begins with background removal using the `rembg` library, which efficiently isolates the subject from the background. The next step involves inpainting the isolated subject into a new context or environment using the `diffusers` library and the Stable Diffusion model. This architecture is highly adaptable and can be extended to various image processing and manipulation applications. By breaking down the process into manageable steps, we ensure a smooth and efficient workflow that produces high-quality results every time.

## Tools/Models Used

We have carefully selected the following tools and models to achieve the best results for our virtual try-on application:

- **Background Removal:** The `rembg` library is employed to accurately remove the background from images, leaving only the subject. This step is crucial for isolating the subject and preparing it for inpainting.
- **Inpainting:** The `diffusers` library with the Stable Diffusion model is used to seamlessly blend the subject into a new background or environment. This allows us to place the subject in various settings, providing a realistic preview of how the subject would look in different contexts.
- **Web Interface:** Streamlit is utilized to create a user-friendly web interface, allowing users to easily upload images and view the inpainting results. The interface is designed to be intuitive and accessible, ensuring a smooth user experience.



## Example

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

- **Upload an image:** Use the file uploader provided in the web interface to upload an image you want to process. You can upload images in various formats including JPG, PNG, and JPEG.

- **Generate the inpainted image:** Click the "Generate" button to create the inpainted image. The application will display the original and the inpainted images side by side. This allows you to compare the results and see the transformation instantly.

- **Output Image:**
  ![Example Input](https://raw.githubusercontent.com/Prajnabhandary/VITON/main/Inpainting/img_3.png)
By following these steps, you can easily generate high-quality inpainted images that provide a realistic preview of the subject in different settings.

Ensure you have a CUDA-compatible GPU and the necessary drivers installed for the best performance. This will significantly speed up the processing time and improve the quality of the generated images.
