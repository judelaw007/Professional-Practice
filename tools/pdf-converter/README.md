# Markdown to PDF Converter

Professional markdown to PDF converter with beautiful formatting that matches GitHub's markdown rendering.

## Features

- ✨ Beautiful header formatting (H1, H2, H3, H4)
- ✨ Professional table rendering with borders and shading
- ✨ GitHub-style markdown theme
- ✨ Automatic page numbers
- ✨ Clean typography and spacing
- ✨ Support for code blocks, lists, blockquotes, and more

## Requirements

```bash
pip3 install weasyprint markdown2
```

## Usage

### Single File Conversion

```bash
python3 tools/pdf-converter/md_to_pdf_converter.py input.md output.pdf
```

### Batch Conversion (Directory)

Convert all markdown files in a directory:

```bash
for file in path/to/directory/*.md; do
    python3 tools/pdf-converter/md_to_pdf_converter.py "$file" "${file%.md}.pdf"
done
```

### Convert to Subfolder

Convert all markdown files and save PDFs to a `pdf` subfolder:

```bash
mkdir -p "path/to/directory/pdf"
for file in path/to/directory/*.md; do
    filename=$(basename "$file" .md)
    python3 tools/pdf-converter/md_to_pdf_converter.py "$file" "path/to/directory/pdf/${filename}.pdf"
done
```

## Quick Instruction for Claude

Copy and paste this instruction in any conversation:

```
Convert all markdown files in [DIRECTORY_PATH] to professionally formatted PDFs using the converter at tools/pdf-converter/md_to_pdf_converter.py.

Requirements:
1. Install dependencies: pip3 install weasyprint markdown2
2. Create a 'pdf' subfolder in the target directory
3. Convert each .md file to PDF with the same filename
4. Commit and push changes when complete

The converter renders markdown beautifully with proper headers, tables, and GitHub-style formatting.
```

## Example

```bash
# Install dependencies
pip3 install weasyprint markdown2

# Convert a single file
python3 tools/pdf-converter/md_to_pdf_converter.py \
    "Professional_Practice_Courses/Part_1/Chapter_1.md" \
    "Professional_Practice_Courses/Part_1/pdf/Chapter_1.pdf"
```

## Output Format

- **Page Size**: A4
- **Margins**: 2.5cm top/bottom, 2cm left/right
- **Font**: System fonts (Segoe UI, Helvetica, Arial)
- **Font Size**: 11pt body, scaled headers
- **Tables**: Bordered with alternating row colors
- **Code**: Monospace with light gray background
