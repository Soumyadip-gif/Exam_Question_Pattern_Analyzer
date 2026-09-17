# 📚 Exam Question Pattern Analyzer

An intelligent web-based application that analyzes exam question papers and identifies **frequently asked topics, similar/repeated questions, keywords, and overall question patterns** using Python, NLP, OCR, and machine learning techniques.

## 🚀 Features

- 📄 Upload **PDF question papers**
- 🖼️ Support **JPG, JPEG, and PNG** question-paper images
- 🔍 Extract text from normal PDFs using **PyMuPDF**
- 🤖 OCR support for scanned PDFs and images using **Tesseract**
- 📝 Automatic question extraction
- 🧹 NLP-based text cleaning and keyword extraction
- 📌 Automatic topic detection
- 🔄 Detect similar/repeated questions using **TF-IDF + Cosine Similarity**
- 📊 Topic frequency analysis
- ⭐ Identify frequently occurring / important topics
- 📈 Interactive topic distribution chart using **Chart.js**
- 🌑 Modern dark-themed web interface
- ⚡ Built with Flask and modular Python processing components

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| NLP | NLTK |
| Machine Learning | Scikit-learn |
| PDF Processing | PyMuPDF |
| OCR | Tesseract OCR, Pytesseract |
| Image Processing | Pillow |
| Visualization | Chart.js |
| Version Control | Git, GitHub |

## 🔄 How It Works

```text
Question Paper
      ↓
PDF / Image Upload
      ↓
Text Extraction
      ↓
OCR for Scanned Documents
      ↓
Question Extraction
      ↓
NLP Processing
      ↓
Keyword & Topic Detection
      ↓
TF-IDF Similarity Analysis
      ↓
Pattern & Topic Frequency Analysis
      ↓
Results Dashboard
