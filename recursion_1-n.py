def number (n,i=1):
    if(i>n):
        return
    else:
        print(i)
        return number(n,i+1)
n = int(input("Please enter number till you want to print: "))
number(n)

"""
output
Please enter number till you want to print: 7
1
2
3
4
5
6
7
"""