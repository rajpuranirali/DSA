# recursion
def fact(num, count=1, factorial=1):
    if count > num:
        return factorial #base case stops function.
    else:
        return fact(num, count + 1, factorial * count) #fun calling it self (recursion)

print(fact(5))  # Output: 120
