# Let the number entered by user is 1234 and user want product of 2 adjacent numbers. Now this 
# program will make list of first 2 numbers entered by user i.e. [1,2] then it will multiply 
# them and store them in a list and it will pop out 1 and 2 from user input.
# Now it will take a number and append it to the list and list will become [1,2,3] then it 
# will pop 1st element and list will be [2,3]. Then their product will be stored in a list and 
# again this process will be repeated till the usr input become empty.
# Then it will print largest value.

mylist=[] # It will store the string that user will enter
usr_input = input('Enter number: ') # Input number from user
usr_input_number = int(input('Enter number of adjacent digits you want to multiply: ')) # Input number of adjacent digit
for digit in usr_input:
    if digit == ' ': # In my case when value was copied space was also copied
        continue
    mylist.append (int(digit)) # otherwise append the number
numbers = [] # Store adjacent numbers
product_of_number_in_mylist = [] # Product of adjacent numbers

# Function to multiply adjacent numbers
def product_of_list():
    product = 1
    if mylist != []: # If list is empty it means that we are at the end of the strig that user enters
        
        for value in numbers:
            product = value*product
        product_of_number_in_mylist.append(product) # Append the number in list
        
        # Function to add and remove number in numbers and mylist
        append_and_remove()
        product_of_list() # Function call
    return product_of_number_in_mylist # List of multiples

# Function to add and remove number in numbers and mylist
def append_and_remove():
    if mylist != []:
        numbers.append(mylist[0]) # Add the element in list
    
        mylist.pop(0) # Remove that element because we have used it
        numbers.pop(0) # remove the first element because we have stored it's product
    return numbers

# Take adjacent numbers
for step in range(0,usr_input_number):
    numbers.append(mylist[step]) # append adjacent numbers
for step in range(0,usr_input_number):
    mylist.pop(0) # Remove numbers from starting

# Calling function
product_of_list()
print(max(product_of_number_in_mylist))
