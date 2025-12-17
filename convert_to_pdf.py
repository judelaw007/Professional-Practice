#!/usr/bin/env python3
import os
import sys
import markdown
from weasyprint import HTML, CSS
from pathlib import Path

def convert_markdown_to_pdf(md_file_path, output_pdf_path):
    """Convert a markdown file to PDF with proper formatting."""

    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML with extensions
    html_content = markdown.markdown(
        md_content,
        extensions=[
            'extra',
            'codehilite',
            'tables',
            'fenced_code',
            'toc'
        ]
    )

    # Add CSS styling for better PDF appearance
    css_style = """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
        }
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-top: 30px;
        }
        h2 {
            color: #34495e;
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 8px;
            margin-top: 25px;
        }
        h3 {
            color: #34495e;
            margin-top: 20px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        table, th, td {
            border: 1px solid #bdc3c7;
        }
        th {
            background-color: #3498db;
            color: white;
            padding: 12px;
            text-align: left;
        }
        td {
            padding: 10px;
        }
        tr:nth-child(even) {
            background-color: #ecf0f1;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        blockquote {
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin-left: 0;
            color: #555;
            font-style: italic;
        }
        ul, ol {
            margin: 15px 0;
            padding-left: 30px;
        }
        li {
            margin: 8px 0;
        }
        @page {
            size: A4;
            margin: 2cm;
        }
    </style>
    """

    # Combine HTML with CSS
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        {css_style}
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Convert HTML to PDF
    HTML(string=full_html).write_pdf(output_pdf_path)
    print(f"Converted: {os.path.basename(md_file_path)} -> {os.path.basename(output_pdf_path)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_to_pdf.py <markdown_directory>")
        sys.exit(1)

    md_directory = sys.argv[1]
    pdf_directory = os.path.join(md_directory, 'pdf')

    # Ensure PDF directory exists
    os.makedirs(pdf_directory, exist_ok=True)

    # Find all markdown files
    md_files = list(Path(md_directory).glob('*.md'))

    if not md_files:
        print(f"No markdown files found in {md_directory}")
        sys.exit(1)

    print(f"Found {len(md_files)} markdown file(s) to convert")

    # Convert each markdown file
    for md_file in sorted(md_files):
        pdf_filename = md_file.stem + '.pdf'
        pdf_path = os.path.join(pdf_directory, pdf_filename)

        try:
            convert_markdown_to_pdf(str(md_file), pdf_path)
        except Exception as e:
            print(f"Error converting {md_file.name}: {str(e)}")

    print(f"\nConversion complete! PDFs saved to: {pdf_directory}")

if __name__ == '__main__':
    main()
