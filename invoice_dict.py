dictData={'vendor':'Multi Marketings','amount':5000,'date':'26/11/2026'}
print(dictData['vendor'])
print(dictData['amount'])
dictData.setdefault('status','New')
for k,v in dictData.items():
    print(f"{k}:{v}")
