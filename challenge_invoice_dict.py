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
for i in dictData:
        print(f"{i['vendor']} - {i['amount']} - {check_amount(i['amount'])}")
    
