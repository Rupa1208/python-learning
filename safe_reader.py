import json
def check_amount(amount):
    try:
        amount = float(amount)
        if amount>50000:
            return "Very high value - needs director approval"
        elif amount>10000:
            return "High value - needs review"
        else:
            return"Normal - auto approve"
    except (ValueError, TypeError):
        return "Invalid amount"
def load_invoices(filename):
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {filename} not found")
    except json.JSONDecodeError:
        print(f"File {filename} has invalid JSON")
    return []

invoices = load_invoices("invoices.json")
for invoice in invoices:
    try:
        print(f"{invoice['vendor']} - {invoice['amount']} - {check_amount(invoice['amount'])}")
    except KeyError as error:
        print(f"Missing field - {error}")
