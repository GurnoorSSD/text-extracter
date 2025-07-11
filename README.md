# text-extracter

**text-extracter** is a simple and lightweight Python tool that extracts visible text from image files using Optical Character Recognition (OCR) powered by Tesseract and the `pytesseract` library.

---

## Features

- Extract text from JPG, PNG, and other common image formats
- Command-line based for simplicity and portability
- Minimal setup with no unnecessary dependencies
- Works on Windows, macOS, and Linux

---

## How It Works

This script uses the Tesseract OCR engine to process an input image and extract any readable text. It supports printed (typed) text in English by default.

---

## Requirements

- Python 3.x
- [pytesseract](https://pypi.org/project/pytesseract/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

---

## Installation

1. **Install Python dependencies**:

```bash
pip install pillow pytesseract
