# AUTOMATED-REPORT-GENERATION

COMPANY: CODTECH IT SOLUTIONS

NAME: VINDHYA H K

INTERN ID: CT08WOV

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

OUTPUT: 



# Data Analysis and PDF Report Generator:

A simple Python tool to analyze data from CSV files and generate formatted PDF reports with basic statistics and visualizations.

## Overview

This tool allows you to:
- Read and analyze data from CSV files
- Generate basic statistical analysis for numeric columns
- Create simple visualizations (histogram and pie chart)
- Produce a professional PDF report with the analysis results

## Installation

1. Clone or download this repository
2. Install the required dependencies:


pip install pandas matplotlib fpdf numpy


## Files Included

- `simple-data-report.py`: The main script for analyzing data and generating PDF reports
- `simple-sample-data.py`: A utility script to generate sample data for testing

## Usage

### Generating Sample Data (optional)

If you don't have a dataset to analyze, you can generate sample data:


python simple-sample-data.py


This will create a file called `sample_data.csv` with random data.

### Generating a Report

To analyze your data and create a PDF report:


python simple-data-report.py


When prompted:
1. Enter the path to your CSV file (e.g., `sample_data.csv` or your own data file)
2. Enter a name for your PDF report (or press Enter to use the default `report.pdf`)

The script will:
- Analyze your data
- Create visualization charts
- Generate a PDF report
- Save the report to the specified filename

## Report Contents

The PDF report includes:

1. **Data Summary**
   - File name
   - Number of rows and columns
   - List of column names

2. **Statistical Analysis**
   - Basic statistics for each numeric column (min, max, mean, median)

3. **Visualizations**
   - Histogram for a numeric column
   - Pie chart for a categorical column (if available)

## Customization

You can modify the scripts to:
- Change the types of visualizations
- Add more statistical metrics
- Format the PDF differently
- Analyze different types of data files

## Requirements

- Python 3.6 or higher
- pandas
- matplotlib
- fpdf
- numpy

## License

This project is available for free use and modification.
