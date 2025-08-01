
# Print name N times using recursion
def print_name(n, name):
    if n == 0:
        return  # base case
    print(name)
    print_name(n - 1, name)  # recursive call

print_name(10, "Tom")



def name(i,n,user_name):

    if i > n:
        return
    else:
        print(user_name)
        return name(i+1,n,user_name)

n = int(input("Please Enter number: "))
user_name = str(input("Provide User name: "))
name(1,n,user_name)

"""
Output:
Tom
Tom
Tom
Tom
Tom
Tom
Tom
Tom
Tom
Tom
Please Enter number: 5
Provide User name: Jerry
Jerry
Jerry
Jerry
Jerry
Jerry
"""