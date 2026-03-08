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
    if i%15=0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        
