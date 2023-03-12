# Question 1:
def hello_name(user_name):
    print(f"Hello {user_name}!")

# Question 2:
def first_odds():
    for i in range(1,101):
        if i %2==0:
            continue
        else:
            print(i)

# Question 3:
def max_num_in_list(a_list):
    print(max(a_list))

my_list = [1, 3, 53, 6, 7,4, 24]



# Question 4:
def is_leap_year(a_year):
    if a_year % 4==0 or a_year%400 ==0:
        return True
    else:
        return False
    
# Question 5:
def is_consecutive(a_list):
    for i in a_list:
        if [i]+1 == [i]:
            return True
        else:
            return False
    
    
        
        

my_list2 = [1, 2, 3, 4, 5, 7]
print(is_consecutive(my_list2))

# I had a harder time with this one.
