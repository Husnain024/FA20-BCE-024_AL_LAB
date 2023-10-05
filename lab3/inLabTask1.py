# Function definition
def count_even_numbers(number_list): 
    # Initialize counter variable 
    even_count = 0  
    # Loop through each number in the list 
    for num in number_list:
        # Check if the number is even
        if num % 2 == 0:
            even_count += 1
    # Return the count of even numbers   
    return even_count

# Test cases 
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [11, 13, 15, 17]
numbers3 = []  # Empty list
 
# Display results
print(count_even_numbers(numbers1))  # Expected output: 5
print(count_even_numbers(numbers2))  # Expected output: 0
print(count_even_numbers(numbers3))  # Expected output: 0
