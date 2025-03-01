import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
from datetime import datetime

def analyze_data(file_path):
    """
    Read data from a CSV file and perform basic analysis
    """
    # Read the data
    df = pd.read_csv(file_path)
    
    # Basic analysis
    analysis = {
        'file_name': os.path.basename(file_path),
        'row_count': len(df),
        'column_count': len(df.columns),
        'columns': list(df.columns),
        'dataframe': df
    }
    
    # Get statistics for numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    stats = {}
    for col in numeric_cols:
        stats[col] = {
            'min': df[col].min(),
            'max': df[col].max(),
            'mean': df[col].mean(),
            'median': df[col].median()
        }
    analysis['stats'] = stats
    
    return analysis

def create_charts(analysis, output_folder="charts"):
    """
    Create simple charts for the report
    """
    # Create folder for charts if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    df = analysis['dataframe']
    chart_paths = []
    
    # Create bar chart for first numeric column
    numeric_cols = df.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        plt.figure(figsize=(8, 4))
        df[col].plot(kind='hist', title=f'Distribution of {col}')
        chart_path = f"{output_folder}/histogram.png"
        plt.savefig(chart_path)
        plt.close()
        chart_paths.append(chart_path)
    
    # Create pie chart for first categorical column (if exists)
    categorical_cols = df.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        col = categorical_cols[0]
        counts = df[col].value_counts()
        plt.figure(figsize=(8, 4))
        counts.plot(kind='pie', autopct='%1.1f%%', title=f'Distribution of {col}')
        chart_path = f"{output_folder}/piechart.png"
        plt.savefig(chart_path)
        plt.close()
        chart_paths.append(chart_path)
    
    return chart_paths

def generate_report(analysis, chart_paths, output_file="report.pdf"):
    """
    Create a simple PDF report with the analysis and charts
    """
    # Initialize PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Set up fonts
    pdf.set_font("Arial", "B", 16)
    
    # Title
    pdf.cell(0, 10, "Data Analysis Report", ln=True, align="C")
    pdf.cell(0, 10, f"File: {analysis['file_name']}", ln=True, align="C")
    pdf.cell(0, 10, f"Generated: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align="C")
    
    # Basic info
    pdf.ln(10)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "1. Data Summary", ln=True)
    
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Number of rows: {analysis['row_count']}", ln=True)
    pdf.cell(0, 10, f"Number of columns: {analysis['column_count']}", ln=True)
    pdf.cell(0, 10, f"Columns: {', '.join(analysis['columns'][:5])}{'...' if len(analysis['columns']) > 5 else ''}", ln=True)
    
    # Statistics
    pdf.ln(10)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "2. Statistical Analysis", ln=True)
    
    pdf.set_font("Arial", "", 12)
    for col, stats in analysis['stats'].items():
        pdf.ln(5)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, f"Statistics for {col}:", ln=True)
        pdf.set_font("Arial", "", 12)
        for stat, value in stats.items():
            pdf.cell(0, 10, f"{stat}: {value:.2f}", ln=True)
    
    # Charts
    if chart_paths:
        pdf.ln(10)
        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, "3. Visualizations", ln=True)
        
        for i, chart_path in enumerate(chart_paths):
            pdf.ln(5)
            pdf.set_font("Arial", "", 12)
            pdf.cell(0, 10, f"Chart {i+1}:", ln=True)
            pdf.image(chart_path, x=20, w=170)
            pdf.ln(5)
    
    # Save the PDF
    pdf.output(output_file)
    return output_file

def main():
    """
    Main function to run the script
    """
    print("Simple Data Analysis and Report Generator")
    
    # Ask for input file
    file_path = input("Enter the path to your CSV file: ")
    
    # Set output file name
    output_file = input("Enter name for the PDF report (default: report.pdf): ")
    if not output_file:
        output_file = "report.pdf"
    
    # Process the data
    print("Analyzing data...")
    analysis = analyze_data(file_path)
    
    print("Creating charts...")
    chart_paths = create_charts(analysis)
    
    print("Generating PDF report...")
    report_path = generate_report(analysis, chart_paths, output_file)
    
    print(f"Report successfully generated: {report_path}")

if __name__ == "__main__":
    main()