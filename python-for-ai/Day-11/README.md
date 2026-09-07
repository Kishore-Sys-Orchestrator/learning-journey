# Day-11 QR Code Generator

I built an interactive project — a **QR Code Generator**.  
This program lets you create QR codes for multiple links in one go, with options to customize colors and filenames.

## Features:
- Generate QR codes for multiple URLs at once
- User‑defined QR file names
- Optional color customization (foreground & background)
- Continuous generation until exit
- Input validation for choices

## Concepts Practiced:
1. `qrcode` library usage
2. String methods (`.lower()`, `.strip()`, `.split()`)
3. `while` Loop for continuous execution
4. `for` Loop with `enumerate()`
5. Conditional statements (`if / elif / else`)
6. User input handling
7. File saving with custom names

## How to run?

```bash
python qr-code-generator.py
```

## Example output:

```text
Want to generate QR code (y/n): y
Enter all URL's separated by comma: This is the code to generate QR-code 
Enter qr name for 'This is the code to generate QR-code': introduction.png
Want to edit colors (y/n): y
Enter the color for your QR: blue
Enter color for background of QR: white
Want to continue generating (y/n): n
```