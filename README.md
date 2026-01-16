# 📝 Text Summarization Console Application (Bulgarian Texts)

## 📌 Project Description

This project is a **console-based text summarization application** implemented in **Python**.  
It performs **extractive text summarization** using a **classic Information Retrieval approach (TF-IDF)**.

The application works with **Bulgarian-language texts** (e.g. news articles from the **SemEval** dataset) and allows the user to:

- Select a document to summarize
- Choose the desired summary length (**short / medium / long**)
- Generate multiple summaries without restarting the program

---

## 🧠 Approach Overview

The summarization process consists of the following steps:

1. The selected document is split into sentences
2. Each sentence is represented using **TF-IDF**
3. Sentences are scored by summing their TF-IDF weights
4. The top-ranked sentences are selected based on the chosen summary length
5. The original sentence order is preserved in the final summary

A custom list of **Bulgarian stopwords** is applied to reduce the influence of frequent function words.

---

## 🗂 Project Structure

```
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
```

---

## ⚙️ Requirements

- **Python 3.9+**
- **pip** (Python package manager)

### 📦 Python Dependencies

```
nltk
numpy
scikit-learn
```

---

## 🚀 Setup Instructions

### 1️⃣ Download or clone the project
Place the project folder anywhere on your system.

### 2️⃣ (Optional) Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download required NLTK resources (one-time setup)

```bash
python
```

```python
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
exit()
```

### 5️⃣ Add documents

Place Bulgarian text files (`.txt`) in the `data/` folder (UTF-8 encoded).

---

## ▶️ Running the Application

```bash
python summarizer.py
```

---

## 🖥 Example Usage

```
Available documents:
1. doc1.txt
2. doc2.txt

Choose document number: 1
Choose summary length (short / medium / long): short

========== SUMMARY ==========
[Generated summary text]
=============================

Summarize another document? (y/n): y
```

---

## 📏 Summary Length Options

| Option  | Description |
|-------|-------------|
| short  | Very brief summary |
| medium | Moderate-length summary |
| long   | More detailed summary |

---

## 📚 Dataset

The documents are **Bulgarian-language texts** taken from the **SemEval dataset**, commonly used in NLP research.

---

## 🧑‍🎓 Academic Note

This project was developed as a **mini course assignment** for an **Information Retrieval 2025/2026** course.


This application demonstrates how **basic Information Retrieval techniques** can be applied to **text summarization** using a lightweight and transparent approach.
