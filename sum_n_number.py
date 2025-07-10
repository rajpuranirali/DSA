
#when i<n it will execute else block.
# When i>n it will execute if block and return value of add. 
def sum(n,i =0,add=0):
    if(i>n):
        return add 
    else:
        add = add + i
        print(add)
        return sum(n,i+1,add)
        

print("sum of given numbers ",sum(3))

"""
Output: 

0
1
3
6
sum of given numbers  6

"""