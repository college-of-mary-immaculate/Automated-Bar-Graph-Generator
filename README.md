# Automated-Bar-Graph-Generator

## What

This project automates the generation of bar graphs from data stored in Excel files (.xlsx). The program monitors the current directory for new Excel files and, upon detecting one, reads the data from the file and generates a bar graph for each row. Each graph is saved as a .jpg file, organized into a separate subfolder for each Excel file.

### Features:
- Monitors the directory for new .xlsx files.
- Automatically generates bar graphs for each row in the Excel file.
- Saves graphs in subfolders to avoid file mix-ups.
- Bar graphs are sorted in increasing order for better data representation.

## Requirements

### Software Requirements:
- Python 3.x
- Libraries:
  - pandas: For reading Excel files.
  - matplotlib: For generating bar graphs.
  - numpy: For sorting data and color mapping.

### Install the required libraries:

To install the required Python libraries, run:

pip install pandas matplotlib numpy

### File Requirements:
  - An Excel file (.xlsx) with at least two columns.
  - The first column should contain titles (or row names).
  - The subsequent columns should contain numeric data for plotting

## How to Use

1. Prepare Your Excel File
Make sure your Excel file is in the format:
  - Row 1: Column headers (ignored by the script).
  - Column 1: Row names (these will be used as graph titles).
  - Remaining Columns: Numeric data to plot.

2. Run the Script
Simply place the script in the directory where you want to monitor for Excel files, then run it using:
python automatedBarGraph.py

3. Place Excel Files
Once the script is running, drop your .xlsx files into the same directory. The script will automatically detect new files, process the data, and generate the bar graphs.

4. Access the Output
The generated bar graphs will be saved as .jpg files inside a folder named "Automated Bar Graphs". Each Excel file will have its own subfolder named after the file (excluding the extension), and each graph will be named after the row title.

## Credits

This script was developed using:
- Pandas: A Python library for data manipulation and analysis.
- Matplotlib: A Python 2D plotting library which produces publication-quality figures.
- NumPy: A Python library used for numerical computations.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software as long as you include the original license and attribution.
