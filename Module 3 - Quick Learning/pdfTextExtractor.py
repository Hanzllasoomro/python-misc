from PyPDF2 import PdfReader

# ✅ Provide the correct path to your PDF file
pdf_path = "E:\\Resume7.pdf"  # Replace with your actual file path

try:
    # Open and read the PDF
    reader = PdfReader(pdf_path)

    # Get the first page
    page = reader.pages[0]

    # Extract text from the page
    text = page.extract_text()

    if text:
        print("✅ Extracted Text:\n")
        print(text)
    else:
        print("⚠️ No text found on the first page.")

except FileNotFoundError:
    print(f"❌ File not found: {pdf_path}")
except Exception as e:
    print(f"❌ An error occurred: {e}")
