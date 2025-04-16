# Client Receipt Generator (PDF)
from fpdf import FPDF
import datetime

def generate_receipt(client, items):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Receipt", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Client: {client}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {datetime.date.today()}", ln=True)
    pdf.ln(5)
    total = 0
    for item, price in items:
        pdf.cell(200, 10, txt=f"{item} - ${price:.2f}", ln=True)
        total += price
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Total Paid: ${total:.2f}", ln=True)
    filename = f"receipt_{client.replace(' ', '_').lower()}.pdf"
    pdf.output(filename)
    print(f"✅ Receipt saved as {filename}")

if __name__ == "__main__":
    generate_receipt("Node2 Client", [("Product A", 49.99), ("Product B", 19.95)])
