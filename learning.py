#Reverse a String 
#Write a function that takes a string like "hello" and returns it reversed: "olleh". Don't use a built-in reverse method.
def reverse_string(s):
    result=""

    for i in range(len(s)-1,-1,-1):
        result += s[i]
    return result

#to test
print(reverse_string("Hello"))

#FizzBuzz
#Print numbers 1 to 100. If divisible by 3 → print "Fizz". If by 5 → "Buzz". If by both → "FizzBuzz". Otherwise print the number.
for i in range(1,101):
    if i%15 == 0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#Check if a String is a Palindrome
#Return True if a string reads the same forwards and backwards. e.g. "racecar" → True, "hello" → False. Ignore spaces and uppercase.

def is_it_palindrome(s):
    s = s.lower().replace(" ","")

    left = 0
    right=len(s)-1

    while left<right:
        if s[left] != s[right]
        return False

    left += 1
    right -= 1

    return True     
