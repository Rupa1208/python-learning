def check_amount(amount):
    if amount>50000:
        return "Very high value - needs director approval"
    elif amount>10000:
        return "High value - needs review"
    else:
        return"Normal - auto approve"
    
listData=[5000, 12000, 60000, 800, 15000]
for i in listData:
    print(str(i)+'->'+check_amount(i))
