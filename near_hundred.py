#Given an int n, return True if it is within 
# 10 of 100 or 200. Note: abs(num) computes the 
# absolute value of a number.

#
# this is not the correct way, input given 
# are not exacts outputs##
def near_hundred(n):
    if n%10==0 or n%100==0 or n%200==0:
        return True
    else:
        return False
    

#BEST SOLUTION

def near_hundred(n):
    if abs(100-n)<=10 or abs(200-n) <=10:
        return True
    else:
        return False
    
x=near_hundred(50)
print(x)


