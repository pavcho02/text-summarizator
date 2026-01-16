# Text Summarization Console Application (Bulgarian Texts)

## Project Description

This project is a simple console-based text summarization application implemented in Python.
It performs extractive text summarization using a classic Information Retrieval approach (TF-IDF).

The application works on Bulgarian-language texts (e.g. news articles from the SemEval dataset) and allows the user to:
- Select a document to summarize
- Choose the desired summary length (short, medium, long)
- Generate summaries multiple times without restarting the program

The goal of the project is to demonstrate a simple, interpretable, and language-independent summarization method,
suitable for a homework(mini course project) assignment.

---

## Approach Overview

The summarization process follows these steps:

1. The selected document is split into sentences
2. Each sentence is represented using TF-IDF
3. Sentences are scored based on the sum of their TF-IDF weights
4. The top-ranked sentences are selected according to the chosen summary length
5. The original sentence order is preserved in the final summary

A custom list of Bulgarian stopwords is used to reduce the influence of frequent function words.

---

## Project Structure

text-summarization-project/
│
├── summarizer.py          # Main application
├── bg_stopwords.py        # Bulgarian stopword list
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── data/
    ├── doc1.txt
    ├── doc2.txt
    └── doc3.txt

---

## Requirements

- Python 3.9 or higher
- pip (Python package manager)

### Python Libraries

The required libraries are listed in requirements.txt:

nltk  
numpy  
scikit-learn  

---

## Setup Instructions

### 1. Clone or download the project
Place the project folder anywhere on your system.

### 2. (Optional but recommended) Create a virtual environment

python -m venv venv

Activate it:

Windows:
venv\Scripts\activate

Linux / macOS:
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Download required NLTK resources (one-time setup)

Run Python in the terminal:

python

Then execute:

import nltk  
nltk.download("punkt")  
nltk.download("punkt_tab")  
exit()

### 5. Add documents

Place your Bulgarian text files (.txt) inside the data/ folder.
The texts should be UTF-8 encoded and contain plain text only.

---

## Running the Application

From the project root directory:

python summarizer.py

---

## Example Usage

Available documents:
1. doc1.txt
2. doc2.txt

Choose document number: 1  
Choose summary length (short / medium / long): short  

========== SUMMARY ==========  
[Generated summary text here]  
=============================  

Summarize another document? (y/n): y

---

## Summary Length Options

short  – very brief summary  
medium – moderate-length summary  
long   – more detailed summary

---

## Dataset

The documents used in this project are Bulgarian-language texts taken from the SemEval dataset,
which is commonly used for research and evaluation in Natural Language Processing tasks.

---

## Key Characteristics

- Console-based interface
- Classic IR-based summarization (TF-IDF)
- Language-aware preprocessing (Bulgarian stopwords)

---

## Academic Note

This project was developed as a homework(mini course project) assignment for an Information Retrieval 2025/2026.
