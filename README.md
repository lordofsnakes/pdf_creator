# Blockchain Course Worksheet Generator

This is a Python tool designed to automatically generate professional, academic-style PDF worksheets for the Web3 Talents Blockchain Fundamentals course. 

Instead of manually formatting documents every week, this script uses a simple "Template System." You just paste your raw text into the configuration section at the top of the script, and it automatically formats and generates two separate PDFs: one for the General Task and one for the Group Tasks.

## Prerequisites

- **Python 3.x** installed on your computer.
- The **fpdf2** library (Note: Do not install the old `fpdf` library, it must be `fpdf2`).

## Installation

1. Download or clone this project to your computer.
2. Open your terminal or command prompt (or the terminal in PyCharm).
3. Install the required PDF library by running: `pip install fpdf2`
4. **Important:** Place your organization's logo in the same folder as the script and name it `logo.png`. If you don't have a logo, the script won't crash; it will simply place a `[LOGO]` text box placeholder in the top left corner.

## How to Use

1. Open the Python script in your code editor (e.g., PyCharm).
2. At the very top of the file, locate the **"1. PASTE YOUR TEXT HERE FOR THE NEW WEEK"** section.
3. Update the variables for the current week. All you have to do is replace the text inside the quotation marks for:
   - `SHEET_NUMBER` (e.g., "3")
   - `SHEET_TOPIC` (e.g., "Wallets & P2P Networks")
   - `GENERAL_TASK_STEPS`, `GENERAL_TASK_CHEAT_SHEET`, etc.
   - `GROUP_TASKS`
4. Save the file.
5. Run the script by clicking the "Play/Run" button in PyCharm, or by typing `python pdf_creator.py` in your terminal.
6. The script will instantly generate two freshly formatted PDF files in the exact same folder:
   - `Sheet_X_General_Task.pdf`
   - `Sheet_X_Group_Tasks.pdf`

## Formatting Rules inside the Text

- You can use standard hyphens (`-`) for bullet points.
- You can use standard Markdown links in the text (e.g., `[Link Text](https://www.example.com)`) and they will be rendered correctly in the PDF as clickable links.
- The script automatically handles page breaks, spacing, and styling so you don't have to worry about the layout breaking when you add long paragraphs.