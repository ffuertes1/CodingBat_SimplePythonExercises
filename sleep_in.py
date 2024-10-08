#We are given 2 parameters in the function and we need to 
# establish if the return value is True or False
# The parameters week day and vacation must say  
# if we are in weekday but not in vacation return False
# if we are on weekday and in vacation we are sleep in
# otherwise return false
# 
# We can start with an if statement with an OR operator
# 
# ##

def sleep_in(weekday, vacation):
    if weekday==False or vacation==True:
        return True
    else:
        return False
x=sleep_in(True,False)
print(x)

#Other easy solution could be just returning
# the negative value of the parameters given as this
# ##

def sleep_in2(weekday, vacation):
    return (not weekday or vacation)
x=sleep_in2(True,False)
print(x)


