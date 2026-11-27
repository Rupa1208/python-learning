def check_amount(amount):
    if amount>50000:
        return "Very high value - needs director approval"
    elif amount>10000:
        return "High value - needs review"
    else:
        return"Normal - auto approve"
import os,json
openInvoicesJson=open("invoices.json")
invoicesJson=openInvoicesJson.read()
pythonVal=json.loads(invoicesJson)
for vendors in pythonVal:
    vendors["status"]=check_amount(float(vendors["amount"]))
out=open("invoices_out.json", "w")
out.write(json.dumps(pythonVal,indent=2))
#indent=2 formats the data properly
openInvoicesJson.close()
out.close()
