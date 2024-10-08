# Exercise: We have a loud 
# talking parrot. The "hour" parameter is the 
# current hour time in the range 0..23. We are in trouble 
# if the parrot is talking and the hour is before 7 or after 20. 
# Return True if we are in trouble.

def parrot_trouble(talking, hour):
    return bool (hour<7 and talking==True) or (hour>20 and talking==True)
x=parrot_trouble(True,6)
print(x)