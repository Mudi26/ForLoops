# Prompt the user to enter a symbol
symbol = input("Enter a symbol: ")


# Prompt the user to enter the number of times to print the symbol
count = input("How many times do you want to print it: ")

# Convert the count to an integer
count = int(count)

# Use a for loop to print the increasing part of the pattern

for i in range(1, count+1):
    print(symbol * i)

# Use a for loop to print the decreasing part of the pattern

for i in range(count-1, 0, -1):
    print (symbol*i)#abc

#Tester
