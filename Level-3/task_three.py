"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def generate_invoice(receipt_string: str) -> str:
    """Generate an invoice from a receipt string."""
    invoice_lines = ["VAT RECEIPT", ""]
    total_no_vat = 0
    total_with_vat = 0
    has_items = False

    # Process each line of the receipt string
    for line in receipt_string.splitlines():
        if line.startswith("Total:"):
            total_with_vat = float(line.split("£")[1])
        elif " - £" in line:
            has_items = True

            item_name, price_str = line.rsplit(" - £", 1)
            price_with_vat = float(price_str)

            price_no_vat = round(price_with_vat * 0.8, 2)
            total_no_vat += price_no_vat

            invoice_lines.append(f"{item_name} - £{price_no_vat:.2f}")

    total_no_vat = round(total_no_vat, 2)
    vat_amount = round(total_with_vat - total_no_vat, 2)

    if has_items:
        invoice_lines.append("")

    # Add the totals to the invoice
    invoice_lines.append(f"Total: £{total_no_vat:.2f}")
    invoice_lines.append(f"VAT: £{vat_amount:.2f}")
    invoice_lines.append(f"Total inc VAT: £{total_with_vat:.2f}")

    return "\n".join(invoice_lines)


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    invoice = generate_invoice(receipt_string)

    print("```")
    print(invoice)
    print("```")
