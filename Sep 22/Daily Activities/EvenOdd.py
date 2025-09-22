def check_num(num):
    if num%2==0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

number=int(input("Enter a number: "))
result=check_num(number)
print(result)

'''for i in range(1,6):
    print(i)'''




