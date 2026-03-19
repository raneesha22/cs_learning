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

#Fibonacci Sequence

def fibonacci(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    
    a=0
    b=1

    for _ in range (2,n+1):
        a=b
        b=a+b

        return b
    


#Anagram check
#same letters , different order

#first of all if the length doesnt match then return false , then make them into 2 lists and iterate trough one against the other and remove one by one 

def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    s1 = list(s1)
    s2 = list(s2)

    for char in s1:
        if char in s2:
            s2.remove(char)
        else:
            return False
        
    return True


#Find the largest number in a list without built in max function

def is_largest(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num
        
        return largest


#Count Occurences of each element 

#how my though process worked 

def count_occurence(items):
    counts ={}

    for item in items:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
    return counts

#what claude gave me

def count_occurence(items):
    counts = {}

    for item in items:
        counts[item] = counts.get(item,0) + 1

    return counts


#Rotate a list by k-steps

#so for example if we have [1,2,3,4,5] and k=2 then we want to return [4,5,1,2,3]
#we can use slicing for this . then concatenate both sliced lists toghther

def rotate(nums,k):
    k=k%len(nums)

    if k ==0:
        return nums
    
    return nums[-k:] + nums[:-k]

#find the missing value in a list of 1 to n
#forst we need to find the sum if nothing was missing 
#then have to find actuayl sum
#then subtract and can find the missing value 

def find_missing(nums):
    n=len(nums)

    expected = n*(n+1)//2
    actual =sum(nums)

    return expected - actual


#Implement a stack and use it to reverese a list

def reverse_with_stack(nums):
    stack=[]

    for num in nums:
        stack.append(num)
    
    result=[]

    for _ in range(len(stack)):
        result.append(stack.pop())


#Valid Parentheses
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.

#Thinking : since here also it returns true if the forst open is closed last , we can use a stack for thi scenario. we push the opening brackets to the stack them in elif we check
#whether the closing brackets matches the last opening brackets in the stack and corresponds to the closing of each one. then we pop the last opening bracket from the stack and continue this process until we reach the end of the string. if at the end of the string the stack is empty then we can say that the parentheses are valid otherwise they are not valid.

def is_valid(s):
    stack = []
    matching = {')':'(', '}':'{', ']':'['}
    
    for ch in s:
        if ch in matching.values():
            stack.append(ch)
        elif ch in matching.keys():
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()
    if len(stack) == 0:
        return True


#Implement a Queue & explain FIFO
#Using a list for this could be inefficient when theres alot of elements , to remove somethign from the front instantly 
#we can use deque from collections
#deque is a double ended queue which allows to append and pop from both ends

from collections import deque

queue = deque()  #creating an emptry list 

queue.append(1)
queue.append(2)
queue.append(3) 

first = queue.popleft() #removing the first element from the queue
print(first) #output: 1

