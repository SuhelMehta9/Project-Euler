# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

# It took 20 seconds to to get output
usr_input = int(input('Enter the number: '))
primeNumber = [2,3,5,7]
number = 9

while usr_input!=value:
    if steps>=usr_input+1:
        break
    
    else:
        for dividor in primeNumber:
            if number%dividor==0:
                break
            elif dividor == primeNumber[-1]:
                primeNumber.append(number)
                
    number = number+2
    #print(number)
    value = len(primeNumber)
print(primeNumber[-1])
