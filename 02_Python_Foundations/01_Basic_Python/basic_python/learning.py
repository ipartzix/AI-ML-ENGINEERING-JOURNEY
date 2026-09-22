import fitz  # PyMuPDF
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the root window
Tk().withdraw()

# Open file dialog to select PDF
file_path = askopenfilename(title="Select a PDF file", filetypes=[("PDF Files", "*.pdf")])

if file_path:
    doc = fitz.open(file_path)
    for i, page in enumerate(doc):
        print(f"\n--- Page {i + 1} ---\n")
        print(page.get_text())
else:
    print("No file selected.")
