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

#Find Duplicate in a List
# 
def is_duplicate(nums):
    seen = set()
    duplicate = set(0
                    
        for num in nums:
            if num in seen:
                duplicate.add(num)
            else:
                seen.add(num)) 
      
        return.list(duplicate)
    
#TWO SUM
#Given a list of numbers and a target, return the indices of the two numbers that add up to the target. e.g. [2,7,11,15], target=9 → [0,1] because 2+7=9.

def two_sum(nums,target):
    seen{}

    for i,num in enumerate(nums):
        complement=target-num

        if complement in seen:
            return[seen[complement],i]
        seen[num]=i

    return[]
