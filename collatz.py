def collatz(num):
    if num%2==0:
        num=num//2
    else:
        num= 3 * num + 1
    print(num)
    return num
user_input=input("Enter Number ")
try:
    num=int(user_input)
    if num==1:
        print ("can't be reduced further")
    elif num<1:
        print ("Invalid number")
    else:
        while num!=1:
            num=collatz(num)
except ValueError as e:
    print(f"Value error: {e}")
