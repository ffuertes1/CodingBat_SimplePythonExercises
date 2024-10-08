# Given a string, return a new string where "not " 
# has been added to the front. However, if the string 
# already begins with "not", return the string unchanged.
# ##

def not_string(str):
    if str.startswith("not"): #startswith() function returns True if a string starts with the specified prefix (string)
        return str
    else:
        return("not " +str )
x=not_string("not Hola Mundo")
print(x)

