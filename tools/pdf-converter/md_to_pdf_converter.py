#!/usr/bin/env python3
"""
Markdown to PDF converter with proper formatting and styling.
Renders markdown with headers, tables, lists, and proper typography.
"""
import sys
import markdown2
from weasyprint import HTML, CSS
from pathlib import Path

def markdown_to_pdf_formatted(markdown_file, pdf_file):
    """
    Convert markdown file to beautifully formatted PDF.
    """
    # Read the markdown file
    with open(markdown_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML with tables support
    html_content = markdown2.markdown(
        md_content,
        extras=[
            'tables',
            'fenced-code-blocks',
            'header-ids',
            'strike',
            'task_list',
            'code-friendly'
        ]
    )

    # CSS styling for professional appearance
    css_style = """
    @page {
        size: A4;
        margin: 2.5cm 2cm;
        @bottom-right {
            content: counter(page);
            font-size: 9pt;
            color: #666;
        }
    }

    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #24292e;
        max-width: 100%;
    }

    h1 {
        font-size: 24pt;
        font-weight: 600;
        margin-top: 24pt;
        margin-bottom: 16pt;
        padding-bottom: 8pt;
        border-bottom: 2px solid #eaecef;
        color: #24292e;
    }

    h2 {
        font-size: 20pt;
        font-weight: 600;
        margin-top: 20pt;
        margin-bottom: 14pt;
        padding-bottom: 6pt;
        border-bottom: 1px solid #eaecef;
        color: #24292e;
    }

    h3 {
        font-size: 16pt;
        font-weight: 600;
        margin-top: 16pt;
        margin-bottom: 12pt;
        color: #24292e;
    }

    h4 {
        font-size: 14pt;
        font-weight: 600;
        margin-top: 14pt;
        margin-bottom: 10pt;
        color: #24292e;
    }

    p {
        margin-top: 0;
        margin-bottom: 10pt;
    }

    strong {
        font-weight: 600;
    }

    em {
        font-style: italic;
    }

    code {
        font-family: 'Courier New', Courier, monospace;
        font-size: 10pt;
        background-color: #f6f8fa;
        padding: 2pt 4pt;
        border-radius: 3pt;
    }

    pre {
        font-family: 'Courier New', Courier, monospace;
        font-size: 10pt;
        background-color: #f6f8fa;
        padding: 12pt;
        border-radius: 4pt;
        overflow-x: auto;
        margin-bottom: 12pt;
    }

    pre code {
        background-color: transparent;
        padding: 0;
    }

    table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 16pt;
        margin-top: 8pt;
    }

    table th {
        background-color: #f6f8fa;
        font-weight: 600;
        padding: 8pt 12pt;
        border: 1pt solid #d0d7de;
        text-align: left;
    }

    table td {
        padding: 8pt 12pt;
        border: 1pt solid #d0d7de;
    }

    table tr:nth-child(even) {
        background-color: #f6f8fa;
    }

    ul, ol {
        margin-top: 0;
        margin-bottom: 10pt;
        padding-left: 24pt;
    }

    li {
        margin-bottom: 4pt;
    }

    blockquote {
        margin: 0;
        padding-left: 12pt;
        border-left: 3pt solid #d0d7de;
        color: #57606a;
    }

    hr {
        height: 2pt;
        padding: 0;
        margin: 24pt 0;
        background-color: #d0d7de;
        border: 0;
    }

    a {
        color: #0969da;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }
    """

    # Create full HTML document
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>{Path(markdown_file).stem}</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Convert HTML to PDF
    HTML(string=full_html).write_pdf(
        pdf_file,
        stylesheets=[CSS(string=css_style)]
    )

    print(f"✓ Converted: {Path(markdown_file).name} -> {Path(pdf_file).name}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python md_to_pdf_pretty.py <input.md> <output.pdf>")
        sys.exit(1)

    markdown_file = sys.argv[1]
    pdf_file = sys.argv[2]

    markdown_to_pdf_formatted(markdown_file, pdf_file)
