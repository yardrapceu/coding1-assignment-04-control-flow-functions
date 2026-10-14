def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: For each value from the list, if the value is more than 1 (in our case 2 and 3), the defined previously function add_one() is used.
# Inside the function, it changes the value that was inputted to +1.
# So we will have 2 outputs printed: 3 and 4. 
# 3 is a result of taking "2" fron the list and using add_one().
# 4 is next result from for-loop - a result of taking "3" fron the list and using add_one().

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: it returns 3. 
# add_one(2) only uses the function with a given number (2 in our case) and does an operation defined in that function (in our case: take input number and add 1).
# Print in the loop in other case, uses the same function, but plugs in a different number (in our case: a few numbers cause its in a loop, thats also the reason why the print() executes a few times).
