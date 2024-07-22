
# Label Artwork Comparison

## Introduction

Label artwork is a vital aspect of product packaging and labeling for consumer products. It guides consumers in making informed choices and helps manufacturers comply with regulatory requirements in various markets. This project applies Computer Vision (CV) techniques to compare label artwork with reference product information, ensuring compliance while reducing validation time and costs. The primary objective is to validate key elements of the label, including the product name, weight claim, and country of origin.

## Solution Architecture

1. **Data Input**: Convert label artwork PDFs to images for further processing.
2. **OCR Processing**: Utilize Paddle OCR to extract text from the converted images.
3. **Text Analysis**: Apply Natural Language Processing (NLP) techniques, such as Named Entity Recognition (NER) and Dependency Parsing, to compare the extracted text with reference information.
4. **Validation**: Identify discrepancies by comparing the OCR-extracted text with the reference product information. Evaluate the accuracy and compliance using the Rouge-L metric.

## Tools/Models Used

### 1. Paddle OCR
Paddle OCR is an advanced optical character recognition (OCR) tool developed by Baidu. It includes a suite of pre-trained models designed for detecting and recognizing text in images. These models can handle various text styles, fonts, and layouts commonly found in product labels. The primary components of Paddle OCR include:

- **Text Detection**: This involves locating text regions within an image. Paddle OCR uses detection algorithms such as EAST (Efficient and Accurate Scene Text Detector) to identify text areas.
- **Text Recognition**: After detecting text regions, Paddle OCR employs recognition models to convert the text within these regions into machine-readable formats. These models are trained on diverse datasets to ensure high accuracy across different languages and text formats.
- **End-to-End Pipeline**: Paddle OCR provides an integrated pipeline that combines text detection and recognition, making it efficient for processing images in a single pass.

### 2. NLP Models
Natural Language Processing models are essential for analyzing and comparing the extracted text with reference information. The specific NLP techniques used in this project include Named Entity Recognition (NER) and Dependency Parsing:

- **Named Entity Recognition (NER)**: NER is a technique used to identify and classify entities within a text into predefined categories such as names of people, organizations, locations, and product attributes (e.g., product name, country of origin, weight claim). This helps in extracting relevant information from the OCR output for comparison with reference data.
- **Dependency Parsing**: Dependency parsing involves analyzing the grammatical structure of a sentence to understand the relationships between words. This technique is used to ensure the extracted text is accurately interpreted and compared with reference information.

### 3. Rouge-L Metric
The Rouge-L metric is a well-known evaluation measure used to assess the quality of text comparison. It stands for Recall-Oriented Understudy for Gisting Evaluation and focuses on the longest common subsequence (LCS) between the compared texts. Rouge-L is particularly suitable for evaluating text matches where exact word sequences are crucial.

- **Longest Common Subsequence (LCS)**: This approach measures the longest sequence of words that appear in both the extracted text and the reference text in the same order. It considers the order of words, making it a robust metric for text comparison in label validation.

## Installation

To set up the necessary tools and models for this project, follow these steps:

### Prerequisites

#### Set Up Paddle OCR
```sh
pip install paddleocr
```

#### Install NLP Libraries
```sh
pip install spacy
python -m spacy download en_core_web_sm
```

## Results

*Details of results should be added here once the implementation is complete.*

## Metrics

ROUGE, specifically ROUGE-Longest Common Sequence (ROUGE-L), is used to evaluate the approach. ROUGE-L measures metrics based on the longest sequence of consecutive words matching the reference text. Among various ROUGE metrics, ROUGE-L is ideal for evaluating text comparisons that require exact matches.

## Limitations

- **OCR Performance**: The OCR struggles to detect text in documents with a large amount of text, especially when converting artwork to PDF. Increasing the DPI (dots per inch) of the image improves accuracy slightly but is insufficient for extracting the full text.
- **Document Partitioning**: Dividing the document into multiple sections helps detect all the text.
- **Misinterpretation of Characters**: Certain characters are misinterpreted, such as “O” being identified as “0”.
- **Symbol Detection**: OCR models fail to detect important symbols needed for artwork validation and regulatory compliance. Training an object detection model to recognize specific symbols is necessary.
