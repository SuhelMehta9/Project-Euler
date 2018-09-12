# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?


usr_input = int(input('Enter the number: '))
primeNumber = [2,3,5,7]
number = 9

value = len(primeNumber)

# Store prime numbers

while value!=usr_input:
    if value==usr_input: # If length of list is equal to user input means the nth prime number that user wants is the last element.
        break
    
    else:
        for dividor in primeNumber: # dividor is the element in list of prime number
            if number%dividor==0:
                break
            elif dividor == primeNumber[-1]: # To check if we have reached at the end of list where prime numbers are stored then
# it would mean that the number is not divisible by any number hence it is a prime number.
                primeNumber.append(number)
                
    number = number+2
    
    #print(number)
    value = len(primeNumber)
print(primeNumber) # Take the last element
