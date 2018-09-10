# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Step 1: Enter the number
number = int(input('Enter the number up to which you want to calculate prime number: '))
# Step 2: Get the prime numbers
def prime(num,number):
    dividor = num;
    dividor = dividor-1
    if num<number:
        while(dividor>2):
            if num%dividor==0:
                
                break;
                
            value = num%dividor
            if(dividor==3):
                primenum.append(num)
                
            dividor = dividor-1
    num = num+2
   
    
    if num>number:
        return primenum # End of step 2
    prime(num,number)
    
primenum = [2,3]
# Calling function to get prime numbers
prime(3,number)

value = 1
# Storing the length of list
listLength = len(primenum)
for step in range(listLength):
    # The logic is we will multiply every element in list till we do not get the largest multiple of each element in primenum
    value = primenum[0]
    multiple = primenum[0]**2
    while multiple < number:
        multiple = multiple*value
        # Now element's value in primenum will be higher than we require
    primenum.append(multiple/value)
    primenum.pop(0) # To pop out the element which is not required

result = 1.0
for steps in range(listLength):
    result = result*primenum[steps]
print(result)
