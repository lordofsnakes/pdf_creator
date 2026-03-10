# Blockchain Course Worksheet Generator

This is a Python tool designed to automatically generate professional, academic-style PDF worksheets for the Web3 Talents Blockchain Fundamentals course. 

Instead of manually formatting documents every week, this script uses a simple "Template System." You just paste your raw text into the configuration section at the top of the script, and it automatically formats and generates two separate PDFs: one for the General Task and one for the Group Tasks.

## Prerequisites

- **Python 3.x** installed on your computer.
- The **fpdf2** library (Note: Do not install the old `fpdf` library, it must be `fpdf2`).

## Installation

1. Download or clone this project to your computer.
2. Open your terminal or command prompt (or the terminal in PyCharm).
3. Install the required PDF library by running:
   ```bash
   pip install fpdf2