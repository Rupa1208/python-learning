def check_amount(amount):
    if amount>50000:
        return "Very high value - needs director approval"
    elif amount>10000:
        return "High value - needs review"
    else:
        return"Normal - auto approve"
    
dictData=[{'vendor':'Multi Marketings','amount':20000,'date':'26/11/2026'},
          {'vendor':'ABC Marketings','amount':50000,'date':'26/11/2026'},
          {'vendor':'SVR Marketings','amount':500,'date':'26/11/2026'}]
total=0
highInvoices=0
for i in dictData:
        total +=i['amount']
        if i['amount']>10000 and i['amount']<=50000:
            highInvoices=highInvoices+1
        print(f"{i['vendor']} - {i['amount']} - {i['date']} - {check_amount(i['amount'])}")
    
print(f"Total Amount = {total}, No.Of High Invoices = {highInvoices}")
