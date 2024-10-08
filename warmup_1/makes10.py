# Solution: is asking to return a true value if the integers
# at least one of them is 10, or if the sum of both is 10
# ##

def makes10(a, b):
    if (a==10 or b==10) or (a+b==10):
        return True
    else:
        return False
x=makes10(5,5)
print(x)

#Other Solution:
# 
# 
# ##

def makes10(a, b):
   return bool((a==10 or b==10) or (a+b==10))
        