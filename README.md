# PDF Merger README

## Introduction
The PDF Merger is a Python script that combines multiple PDF files into a single PDF document. It uses the PyPDF2 library to perform this task efficiently.

## Requirements
Before running the PDF Merger, make sure you have the following prerequisites installed on your system:

- Python: You need to have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

- PyPDF2 library: Install it using pip with the following command:

   ```
   pip install PyPDF2
   ```

## Usage
Follow these steps to use the PDF Merger:

1. Clone or download this repository to your local machine.

2. Place the PDF files you want to merge in the same directory as the script or specify their paths in the `pdffiles` list within the script.

3. Open a terminal or command prompt.

4. Navigate to the directory where you saved the PDF Merger script.

5. Run the code by executing the following command:

   ```
   python pdf_merger.py
   ```

6. The script will combine the specified PDF files into a single PDF document named "merged.pdf" in the same directory.

## Customization
You can customize the script to merge different sets of PDF files by modifying the `pdffiles` list in the script. Simply provide the filenames or paths of the PDFs you want to merge within the list.

```
pdffiles = ["1.pdf", "2.pdf", "3.pdf"]
```

You can also change the output filename by modifying the following line in the script:

```
merger.write("merged.pdf")
```

Replace `"merged.pdf"` with your desired filename.


## Acknowledgments
- This script utilizes the PyPDF2 library for PDF manipulation.
- Created by Virendra Singh

Feel free to contribute to this project or provide feedback. If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/virendra1109).
