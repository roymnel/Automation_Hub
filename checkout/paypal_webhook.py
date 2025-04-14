from flask import Flask, request, jsonify
from fpdf import FPDF
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/paypal/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    payer = data.get("payer", {}).get("name", {}).get("given_name", "Unknown")
    amount = data.get("purchase_units", [{}])[0].get("amount", {}).get("value", "0.00")

    invoice_id = f"INV-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    filename = f"invoices/{invoice_id}.pdf"
    os.makedirs("invoices", exist_ok=True)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Automation Hub Invoice", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Invoice ID: {invoice_id}", ln=True)
    pdf.cell(200, 10, txt=f"Customer: {payer}", ln=True)
    pdf.cell(200, 10, txt=f"Amount Paid: ${amount}", ln=True)
    pdf.output(filename)

    return jsonify({"status": "logged", "invoice": filename})

if __name__ == '__main__':
    app.run(port=5000)
