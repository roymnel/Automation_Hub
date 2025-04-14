# ecommerce_deliver.py
# Advanced delivery script with PDF + email for E-Commerce Automation

import os
import datetime
from fpdf import FPDF
from utils.send_email import send_receipt

def generate_receipt_pdf(output_path="receipt_ecommerce.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_text_color(33, 150, 243)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(200, 10, txt="Automation Hub – E-Commerce Service Receipt", ln=True, align='C')

    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.cell(200, 10, txt="Service: E-Commerce Automation", ln=True)
    pdf.cell(200, 10, txt="Delivery Method: Scripted PDF Receipt", ln=True)
    pdf.cell(200, 10, txt="Price Paid: $139.00", ln=True)

    pdf.output(output_path)
    return output_path

def deliver_service(customer_email):
    print("=== E-COMMERCE SERVICE DELIVERY ===")
    print("[✓] Delivery started...")
    pdf_path = generate_receipt_pdf()

    subject = "Your E-Commerce Automation Receipt"
    body = (
        "Hello,\n\n"
        "Thank you for your purchase of the E-Commerce Automation service from Automation Hub.\n"
        "Please find your receipt attached.\n\n"
        "This message is automatically generated. No response is required.\n"
        "Visit your dashboard for service access and updates.\n\n"
        "Best,\nAutomation Hub"
    )

    send_receipt(customer_email, subject, body, pdf_path)
    print("[✓] Delivery complete.")

if __name__ == "__main__":
    test_email = "customer@example.com"
    deliver_service(test_email)
