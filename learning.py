#Reverse a String 
#Write a function that takes a string like "hello" and returns it reversed: "olleh". Don't use a built-in reverse method.
def reverse_string(s):
    result=""

    for i in range(len(s)-1,-1,-1):
        result += s[i]
    return result

#to test
print(reverse_string("Hello"))