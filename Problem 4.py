# Problem 4: Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

num = 999 # Numbers start from 999
num2 = 999
palindrome = [] # Store palindrome numbers
while num != 99: # We only require 3 digit numbers so if a 2 digit number appears then loop will stop
    while num2 != 99: # Same with this loop also
        result = num*num2 # Multiplying each number 
        orignal = result # It will be use to check palindrome number 
        result = str(result) # It is easy to convert string to list
        result= list(result) 
        result.reverse() # Reverse the number
        result = ''.join(result) # Convert list to string
        result = int(result) # Convert list to integer
        if result == orignal: # if number is palindrome
            palindrome.append(orignal) # Store the number to list(palindrome)
        num2 = num2-1 #decrement the number
    num2 = 999 # When first number is decrreased by one then the value of other number must be 999 to get the desired result
    num = num - 1 # decrease the number
print(max(palindrome)) # Print the largest palindrome number
