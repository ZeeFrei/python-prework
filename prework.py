# Question 1:

def hello_name(user_name):
    '''Takes an input and prints a greeting to the user'''
    print(f"hello_{user_name}!")

name = input("What is your username? ")
hello_name(name)

# Question 2:

def first_odds():
    for i in range(1, 101):
        if i % 2 != 0:
            print(i)

first_odds()

# Question 3:

def max_num_in_list(a_list):
    print(max(a_list))
        
numbers = [20, 10, 40, 0]

max_num_in_list(numbers)

# Question 4:

def is_leap_year(a_year):
    '''Determines if a given year is a leap year.'''
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False 
    print(leap)
        
is_leap_year(2012)

# Question 5:

def is_consecutive(a_list):
    return a_list == list(range(min(a_list), max(a_list)+1))

numbers = [1,2,3,4]
print(is_consecutive(numbers))