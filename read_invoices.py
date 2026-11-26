
def check_amount(amount):
    if amount>50000:
        return "Very high value - needs director approval"
    elif amount>10000:
        return "High value - needs review"
    else:
        return"Normal - auto approve"
total = 0
check_amount_result=[]
with open("invoices.txt") as file:
    for line in file:
        vendor, amount, date = line.strip().split(",")
        amount = float(amount)
        check_amount_result.append(f"{vendor} - {amount} - {date} - "+check_amount(amount))
        total += amount
        print(f"{vendor} - {amount} - {date}")

print(f"Total = {total}")
out=open("summary.txt","w")
for line in check_amount_result:
        out.write(line + "\n")
out.write(f"Total = {total}\n")
out.close()
