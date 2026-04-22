# VisionPDF


**Semantic Image Search System for PDFs**

---

##  Overview

VisionPDF is a system that extracts figures and their captions from PDF documents and enables **semantic search over visual content**. It combines document layout understanding with modern embedding techniques to make diagrams and figures easily searchable.

---

## Features

* Batch processing of multiple PDFs via ZIP upload
* Automatic extraction of figures and diagrams
* Caption detection using pattern-based text analysis
* Semantic search using CLIP-based embeddings
* Export results as Word documents
* Interactive interface built with Streamlit

---

## How It Works

1. Upload ZIP containing PDFs
2. Detect pages with visual content
3. Create reduced PDF (only relevant pages)
4. Parse document structure using Docling
5. Extract images and captions
6. Generate embeddings for images
7. Perform semantic search on extracted images

---

## Tech Stack

* **Python**
* **Streamlit** (Frontend)
* **PyMuPDF** (PDF processing)
* **Docling** (Document parsing)
* **CLIP (Transformers)** (Image-text embeddings)
* **Sentence Transformers**
* **NumPy**
* **Scikit-learn**


---

## Project Structure

```
core/
  ├── pdf_extractor.py
  ├── embedding.py
  ├── search.py
  ├── clip_model.py

utils/
  ├── file_utils.py

app.py
requirements.txt
```

---

## Installation

```bash
git clone https://github.com/your-username/visionpdf.git
cd visionpdf
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

---


## Future Improvements

* Support for scanned PDFs (OCR integration)
* Improved caption detection using ML
* Web deployment for public access
* Faster indexing using vector databases

---

