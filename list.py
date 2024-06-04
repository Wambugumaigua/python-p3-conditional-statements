#even_numbers = []  
#for i in range(11):  
  #  if i % 2 == 0:  
  #      even_numbers.append(i) 
   #     print(even_numbers) 

#generator_expression=(i for i in range(11)if i%2==0)

# Create the generator expression
generator_expression = (i for i in range(11) if i % 2 == 0)

# Iterating over the generator and printing each value
print("Using for loop:")
for number in generator_expression:
    print(number)

# Create the generator expression again since the previous one has been exhausted
generator_expression = (i for i in range(11) if i % 2 == 0)

# Converting the generator to a list and printing the list
even_numbers_list = list(generator_expression)
print("Converted to list:")
print(even_numbers_list)
