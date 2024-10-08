#Given 2 int values, return True if one is 
# negative and one is positive. Except if the parameter 
# "negative" is True, then return True only if both are 
# negative.

# ##
#First solution. Its has a small error that for some inputs its
# giving True and supposed to be False
def pos_neg(a, b, negative):
    if (a<0 or b<0) and (negative==False):
        return True
    elif (a<0 and b<0) and (negative==True):
        return True
    elif (a<0 and b<0) and (negative==False):
        return False
    else:
        return False
x=pos_neg(1,-1,False)
print(x)


#Best Solution:

def pos_neg(a,b,negative):
    if negative:
        return (a<0 and b<0)
    else:
        return (a<0 and b>0) or (a>0 and b<0)
    
    