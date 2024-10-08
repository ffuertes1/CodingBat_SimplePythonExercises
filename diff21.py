#Given an number n, return the difference of the number to though 21
# if n is not less than 21 then i return the double 
# of the difference value
# 
# ##
def diff21(n):
    if n<=21:
        return 21-n
    else:
        return (n-21)*2
x=diff21(19)
print(x)