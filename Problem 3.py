# Problem 3: Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# For prime numbers upto 1 lakh this program took approximately 20 minutes.
#This program can calculate prime numbers up to 10,000
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
        return primenum
    prime(num,number)
    
def more_prime(num,number):
    dividor = num;
    dividor = (dividor-1)/2
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
        return primenum
    prime(num,number)
    
primenum = [3]
prime(3,5000)
#print(primenum)
number = 5000
while number<10000:
    big_prime = primenum[-1]
    
    more_prime(big_prime,(big_prime+4999))
    #print(primenum)
    number = number+5000
    
# To find largest prime factor of number 600851475143
primenum.reverse()
for primeNumber in primenum:
    if 600851475143%primeNumber==0:
        print(primeNumber)
# This program can be developed, if we can make a list of prime numbers starting with 2 and keep dividing a number with prime number 
# to get next prime number. 
        break;
