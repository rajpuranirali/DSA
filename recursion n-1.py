# Print N to 1
def number(n):
    if n<1:
        return
    else:
        print(n)
        return number(n-1)
n = int(input("Please Enter NUmber: "))
number(n)

"""
Output:
Please Enter NUmber: 5
5
4
3
2
1



"""