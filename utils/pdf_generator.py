from fpdf import FPDF
from datetime import datetime

def clean_text(text):
    return text.encode('latin-1', errors='ignore').decode('latin-1')

def create_pdf_report(site_data, comparison_data, ai_tips):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="SEO InsightHub Report", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(200, 10, txt="Website Data:", ln=True)
    pdf.set_font("Arial", size=12)
    for key, value in site_data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(200, 10, txt="AI Improvement Tips:", ln=True)
    pdf.set_font("Arial", size=12)
    for tip in ai_tips:
        safe_tip = clean_text(tip)
        pdf.multi_cell(0, 10, txt=f"- {safe_tip}")

    file_path = "SEO_InsightHub_Report.pdf"
    pdf.output(file_path)
    return file_path
