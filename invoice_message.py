vendor=input("Vendor Name: ")
amount=float(input("Invoice Amount: "))
print(f"Invoice from {vendor} for {amount}")
if amount>50000:
    print("Very high value - needs director approval")
elif amount>10000:
    print("High value - needs review")
else:
    print("Normal - auto approve")
    
