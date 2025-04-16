# Invoice Summary Report
from fpdf import FPDF
import datetime

def generate_invoice(client, items):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Invoice for {client}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {datetime.date.today().isoformat()}", ln=True)
    total = 0
    for item, price in items:
        pdf.cell(200, 10, txt=f"{item}: ${price:.2f}", ln=True)
        total += price
    pdf.cell(200, 10, txt=f"Total: ${total:.2f}", ln=True)
    pdf.output(f"invoice_{client}.pdf")
    print(f"Invoice saved as invoice_{client}.pdf")

if __name__ == "__main__":
    generate_invoice("Example Client", [("Service A", 100), ("Service B", 75)])
