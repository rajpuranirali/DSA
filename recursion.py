# recursion

# factorial 

def fact(num, count=1, factorial=1):
    if count > num:
        return factorial #base case stops function.
    else:
        return fact(num, count + 1, factorial * count) #fun calling it self (recursion)

print(fact(5))  # Output: 120


# fibonaci

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2) # 
    print(fibonacci)
    # return fibonacci(n - 1) + fibonacci(n - 2) # 

# print("10th Fibonacci number:", fibonacci(10))

print(fibonacci(10))  

# # Print the full series up to the 10th term (0 to 9)
# print("Fibonacci series up to 10 terms:")
# for i in range(10):
#     print(fibonacci(i), end=" ") 



