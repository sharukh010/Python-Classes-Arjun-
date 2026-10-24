"""
The number of time we run a loop is called as iterations 
a single iteration is a single execution of a loop 
when we know the number of iterations we go with for loop 
when we don't know the number of iterations we go with while loop 
we use while loop when the loop / iterations are dependent on a condition 
"""
number_of_chips = 300 # potato chips 
users_capacity = int(input("Enter you're capacity (1-300): "))
chips_ate = 0 
"""
here we need to stop when 
chips_ate >= users_capacity and number_of_chips <= 0 
then the opposite condition we should use it in the loop 
chips_ate < user_capacity and number_of_chips > 0 this should be our while loop condition 
"""
while chips_ate < users_capacity and number_of_chips > 0: 
    chips_ate += 1 
    number_of_chips -= 1 

print(f"I ate {chips_ate} number of chips")