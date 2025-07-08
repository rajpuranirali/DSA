def number (n,i=1):
    if(i>n):
        return
    else:
        print(i)
        return number(n,i+1)
n = int(input("Please enter number till you want to print: "))
number(n)