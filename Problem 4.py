# Problem 4: Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

num = 999
num2 = 999
palindrome = []
while num != 99:
    while num2 != 99:
        result = num*num2
        orignal = result
        result = str(result)
        result= list(result)
        result.reverse()
        result = ''.join(result)
        result = int(result)
        if result == orignal:
            palindrome.append(orignal)
        num2 = num2-1
    num2 = 999
    num = num - 1
print(max(palindrome))
