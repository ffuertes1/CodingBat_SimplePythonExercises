#
# [Excersice] We have two monkeys, a and b, and the parameters 
# a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or if 
# neither of them is smiling. Return True if we are 
# in trouble.
# 
# ##

#
# Solution: monkeys a and b are the parameters of the function
# using an if statement either both monkey are smiling or not 
# return true because it means we are in trouble
# if not we return false ##

def monkey_trouble(a_smile, b_smile):
    if a_smile==True and b_smile==True:
        return True
    elif a_smile==False and b_smile==False:
        return True
    else:
        return False
x=monkey_trouble(True,False)
print(x)

# we can do other solution with less lines

def monkey_trouble(a_smile, b_smile):
    return bool(a_smile==b_smile)
x=monkey_trouble(False,False)
print(x)